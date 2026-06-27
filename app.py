#Part 1

import os
from dotenv import load_dotenv

import streamlit as st
import google.generativeai as genai

from ai_summary import generate_summary
from resume_template import generate_resume_html
from pdf_generator import generate_pdf

# ==========================================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv()


# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="AI ATS Resume Builder",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================================
# LOAD CSS
# ==========================================================

def load_css():

    if os.path.exists("style.css"):

        with open("style.css", "r", encoding="utf-8") as css:

            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True
            )


load_css()


# ==========================================================
# GEMINI CONFIGURATION
# ==========================================================

DEFAULT_API_KEY = os.getenv("GEMINI_API_KEY", "")

if DEFAULT_API_KEY:

    genai.configure(api_key=DEFAULT_API_KEY)


# ==========================================================
# SESSION STATE INITIALIZATION
# ==========================================================

DEFAULT_STATE = {

    "generated": False,

    "summary": "",

    "resume_html": "",

    "resume_data": {},

    "skills": [""],

    "education": [
        {
            "degree": "",
            "college": "",
            "university": "",
            "cgpa": "",
            "year": ""
        }
    ],

    "experience": [
        {
            "company": "",
            "designation": "",
            "start_month": "",
            "start_year": "",
            "end_month": "",
            "end_year": "",
            "currently_working": False,
            "responsibilities": ""
        }
    ],

    "projects": [
        {
            "title": "",
            "technology": "",
            "description": "",
            "github": "",
            "live_demo": ""
        }
    ],

    "certifications": [""],

    "languages": [""],

    "achievements": [""]
}


for key, value in DEFAULT_STATE.items():

    if key not in st.session_state:

        st.session_state[key] = value


# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

MONTHS = [

    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"

]

CURRENT_YEAR = 2026

YEARS = [
    str(year)
    for year in range(CURRENT_YEAR + 5, 1980, -1)
]


def add_skill():

    st.session_state.skills.append("")


def add_education():

    st.session_state.education.append(

        {
            "degree": "",
            "college": "",
            "university": "",
            "cgpa": "",
            "year": ""
        }

    )


def add_experience():

    st.session_state.experience.append(

        {
            "company": "",
            "designation": "",
            "start_month": "",
            "start_year": "",
            "end_month": "",
            "end_year": "",
            "currently_working": False,
            "responsibilities": ""
        }

    )


def add_project():

    st.session_state.projects.append(

        {
            "title": "",
            "technology": "",
            "description": "",
            "github": "",
            "live_demo": ""
        }

    )


def add_certification():

    st.session_state.certifications.append("")


def add_language():

    st.session_state.languages.append("")


def add_achievement():

    st.session_state.achievements.append("")

    
#part 2    
# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image("https://img.icons8.com/color/96/resume.png", width=70)

    st.title("AI ATS Resume Builder")

    st.markdown("---")

    st.subheader("🔑 Gemini API")

    user_api_key = st.text_input(
        "Gemini API Key",
        type="password",
        value="",
        help="Leave blank to use the API Key from your .env file."
    )

    if user_api_key.strip():

        genai.configure(api_key=user_api_key.strip())

        st.success("Using Sidebar API Key")

    elif DEFAULT_API_KEY:

        st.success("Using .env API Key")

    else:

        st.warning("No Gemini API Key Found")

    st.markdown("---")

    st.info(
        """
This Resume Builder generates

✅ ATS Friendly Resume

✅ AI Professional Summary

✅ PDF Resume

✅ Modern HTML Resume
"""
    )


# ==========================================================
# PAGE HEADER
# ==========================================================

st.title("📄 AI ATS Resume Builder")

st.caption(
    "Create a Professional ATS-Friendly Resume using Gemini AI"
)

st.divider()


# ==========================================================
# MAIN LAYOUT
# ==========================================================

input_column, preview_column = st.columns(
    [1.15, 0.85],
    gap="large"
)


# ==========================================================
# INPUT COLUMN
# ==========================================================

with input_column:

    st.header("Resume Information")

    st.markdown(
        "Fill in the details below to generate your professional ATS-friendly resume."
    )

    st.divider()


    # ------------------------------------------------------
    # PERSONAL DETAILS
    # ------------------------------------------------------

    with st.expander(
        "👤 Personal Details",
        expanded=True
    ):

        full_name = st.text_input(
            "Full Name *"
        )

        phone = st.text_input(
            "Phone Number *"
        )

        email = st.text_input(
            "Email Address *"
        )

        address = st.text_input(
            "Address"
        )

        linkedin = st.text_input(
            "LinkedIn Profile"
        )

        github = st.text_input(
            "GitHub Profile"
        )

        portfolio = st.text_input(
            "Portfolio Website"
        )

#part 3
        # ==========================================================
    # SKILLS
    # ==========================================================

    with st.expander("💼 Skills", expanded=True):

        st.write("Add your technical and professional skills.")

        for i in range(len(st.session_state.skills)):

            st.session_state.skills[i] = st.text_input(
                f"Skill {i+1} *",
                value=st.session_state.skills[i],
                key=f"skill_{i}"
            )

        if st.button(
            "➕ Add Skill",
            key="add_skill_btn",
            use_container_width=True
        ):
            add_skill()
            st.rerun()


    # ==========================================================
    # EDUCATION
    # ==========================================================

    with st.expander("🎓 Education", expanded=False):

        st.write("Add all your educational qualifications.")

        for i in range(len(st.session_state.education)):

            st.markdown(f"### Education {i+1}")

            education_item = st.session_state.education[i]

            education_item["degree"] = st.text_input(
                "Degree",
                value=education_item["degree"],
                key=f"degree_{i}"
            )

            education_item["college"] = st.text_input(
                "College",
                value=education_item["college"],
                key=f"college_{i}"
            )

            education_item["university"] = st.text_input(
                "University",
                value=education_item["university"],
                key=f"university_{i}"
            )

            col1, col2 = st.columns(2)

            with col1:

                education_item["cgpa"] = st.text_input(
                    "CGPA / Percentage",
                    value=education_item["cgpa"],
                    key=f"cgpa_{i}"
                )

            with col2:

                education_item["year"] = st.selectbox(
                    "Passing Year",
                    YEARS,
                    index=YEARS.index(education_item["year"])
                    if education_item["year"] in YEARS else 0,
                    key=f"year_{i}"
                )

        if st.button(
            "➕ Add Education",
            key="add_education_btn",
            use_container_width=True
        ):
            add_education()
            st.rerun()    

    #part 4    
    # ==========================================================
    # EXPERIENCE
    # ==========================================================

    with st.expander("💼 Experience", expanded=False):

        fresher = st.checkbox(
            "I am a Fresher",
            value=False
        )

        if not fresher:

            st.write("Add your professional experience.")

            for i in range(len(st.session_state.experience)):

                st.markdown(f"### Experience {i+1}")

                exp = st.session_state.experience[i]

                exp["company"] = st.text_input(
                    "Company Name",
                    value=exp["company"],
                    key=f"company_{i}"
                )

                exp["designation"] = st.text_input(
                    "Designation",
                    value=exp["designation"],
                    key=f"designation_{i}"
                )

                st.markdown("#### Duration")

                col1, col2 = st.columns(2)

                with col1:

                    exp["start_month"] = st.selectbox(
                        "Start Month",
                        MONTHS,
                        index=MONTHS.index(exp["start_month"])
                        if exp["start_month"] in MONTHS else 0,
                        key=f"start_month_{i}"
                    )

                    exp["start_year"] = st.selectbox(
                        "Start Year",
                        YEARS,
                        index=YEARS.index(exp["start_year"])
                        if exp["start_year"] in YEARS else 0,
                        key=f"start_year_{i}"
                    )

                with col2:

                    exp["currently_working"] = st.checkbox(
                        "Currently Working Here",
                        value=exp["currently_working"],
                        key=f"current_job_{i}"
                    )

                    if exp["currently_working"]:
                        exp["end_month"] = ""
                        exp["end_year"] = ""  
                        
                    exp["end_month"] = st.selectbox(
                        "End Month",
                        MONTHS,
                        index=MONTHS.index(exp["end_month"])
                        if exp["end_month"] in MONTHS else 0,
                        disabled=exp["currently_working"],
                        key=f"end_month_{i}"
                    )

                    exp["end_year"] = st.selectbox(
                        "End Year",
                        YEARS,
                        index=YEARS.index(exp["end_year"])
                        if exp["end_year"] in YEARS else 0,
                        disabled=exp["currently_working"],
                        key=f"end_year_{i}"
                    )

                exp["responsibilities"] = st.text_area(
                    "Responsibilities",
                    value=exp["responsibilities"],
                    height=150,
                    key=f"responsibilities_{i}"
                )

                st.divider()

            if st.button(
                "➕ Add Experience",
                key="add_experience_btn",
                use_container_width=True
            ):
                add_experience()
                st.rerun()

        else:

            st.info(
                "Experience section will be skipped for freshers."
            )

#part 5
    # ==========================================================
    # PROJECTS
    # ==========================================================

    with st.expander("🚀 Projects", expanded=False):

        st.write("Add your academic and professional projects.")

        for i in range(len(st.session_state.projects)):

            st.markdown(f"### Project {i+1}")

            project = st.session_state.projects[i]

            project["title"] = st.text_input(
                "Project Title *",
                value=project["title"],
                key=f"project_title_{i}"
            )

            project["technology"] = st.text_input(
                "Technologies Used",
                value=project["technology"],
                key=f"project_technology_{i}"
            )

            project["description"] = st.text_area(
                "Project Description",
                value=project["description"],
                height=140,
                key=f"project_description_{i}"
            )

            col1, col2 = st.columns(2)

            with col1:

                project["github"] = st.text_input(
                    "GitHub URL",
                    value=project["github"],
                    key=f"github_{i}"
                )

            with col2:

                project["live_demo"] = st.text_input(
                    "Live Demo URL",
                    value=project["live_demo"],
                    key=f"live_demo_{i}"
                )

            st.divider()

        if st.button(
            "➕ Add Project",
            key="add_project_btn",
            use_container_width=True
        ):
            add_project()
            st.rerun()


    # ==========================================================
    # CERTIFICATIONS
    # ==========================================================

    with st.expander("📜 Certifications", expanded=False):

        for i in range(len(st.session_state.certifications)):

            st.session_state.certifications[i] = st.text_input(
                f"Certification {i+1}",
                value=st.session_state.certifications[i],
                key=f"certification_{i}"
            )

        if st.button(
            "➕ Add Certification",
            key="add_certification_btn",
            use_container_width=True
        ):
            add_certification()
            st.rerun()


    # ==========================================================
    # LANGUAGES
    # ==========================================================

    with st.expander("🌍 Languages", expanded=False):

        for i in range(len(st.session_state.languages)):

            st.session_state.languages[i] = st.text_input(
                f"Language {i+1}",
                value=st.session_state.languages[i],
                key=f"language_{i}"
            )

        if st.button(
            "➕ Add Language",
            key="add_language_btn",
            use_container_width=True
        ):
            add_language()
            st.rerun()


    # ==========================================================
    # ACHIEVEMENTS
    # ==========================================================

    with st.expander("🏆 Achievements", expanded=False):

        for i in range(len(st.session_state.achievements)):

            st.session_state.achievements[i] = st.text_input(
                f"Achievement {i+1}",
                value=st.session_state.achievements[i],
                key=f"achievement_{i}"
            )

        if st.button(
            "➕ Add Achievement",
            key="add_achievement_btn",
            use_container_width=True
        ):
            add_achievement()
            st.rerun()       


#part 6
# ==========================================================
# GENERATE RESUME
# ==========================================================

st.divider()

if st.button(
    "🚀 Generate Resume",
    use_container_width=True,
    type="primary"
):

    # ------------------------------------------------------
    # Mandatory Validation
    # ------------------------------------------------------

    if not full_name.strip():

        st.error("Full Name is required.")
        st.stop()

    if not phone.strip():

        st.error("Phone Number is required.")
        st.stop()

    if not email.strip():

        st.error("Email Address is required.")
        st.stop()

    skills = [

        skill.strip()

        for skill in st.session_state.skills

        if skill.strip()

    ]

    if len(skills) == 0:

        st.error("Please enter at least one skill.")
        st.stop()

    # ------------------------------------------------------
    # Clean Education
    # ------------------------------------------------------

    education = []

    for edu in st.session_state.education:

        if edu["degree"].strip():

            education.append(edu)

    # ------------------------------------------------------
    # Clean Experience
    # ------------------------------------------------------

    experience = []

    if not fresher:

        for exp in st.session_state.experience:

            if exp["company"].strip():

                experience.append(exp)

    # ------------------------------------------------------
    # Clean Projects
    # ------------------------------------------------------

    projects = []

    for project in st.session_state.projects:

        if project["title"].strip():

            projects.append(project)

    # ------------------------------------------------------
    # Clean Optional Lists
    # ------------------------------------------------------

    certifications = [

        cert.strip()

        for cert in st.session_state.certifications

        if cert.strip()

    ]

    languages = [

        lang.strip()

        for lang in st.session_state.languages

        if lang.strip()

    ]

    achievements = [

        ach.strip()

        for ach in st.session_state.achievements

        if ach.strip()

    ]

    # ------------------------------------------------------
    # Resume Dictionary
    # ------------------------------------------------------

    resume_data = {

        "name": full_name,

        "phone": phone,

        "email": email,

        "address": address,

        "linkedin": linkedin,

        "github": github,

        "portfolio": portfolio,

        "summary": "",

        "skills": skills,

        "education": education,

        "experience": experience,

        "projects": projects,

        "certifications": certifications,

        "languages": languages,

        "achievements": achievements

    }

    # ------------------------------------------------------
    # Generate AI Summary
    # ------------------------------------------------------

    with st.spinner("Generating AI Professional Summary..."):

        summary = generate_summary(

            resume_data,

            user_api_key.strip()

            if user_api_key.strip()

            else DEFAULT_API_KEY

        )

    resume_data["summary"] = summary

    # ------------------------------------------------------
    # Generate Resume HTML
    # ------------------------------------------------------

    html = generate_resume_html(resume_data)

    # ------------------------------------------------------
    # Save to Session State
    # ------------------------------------------------------

    st.session_state.generated = True

    st.session_state.summary = summary

    st.session_state.resume_data = resume_data

    st.session_state.resume_html = html

    # ------------------------------------------------------
    # Generate PDF
    # ------------------------------------------------------

    try:

        pdf_bytes = generate_pdf(html)

        st.session_state.resume_pdf = pdf_bytes

    except Exception as e:

        st.error(str(e))

        st.stop()

    st.success("✅ Resume Generated Successfully!")       

#part 7
# ==========================================================
# PREVIEW COLUMN
# ==========================================================

with preview_column:

    st.header("Resume Preview")

    st.markdown(
        "Preview your AI-generated ATS-friendly resume."
    )

    st.divider()

    # ------------------------------------------------------
    # Show Empty State
    # ------------------------------------------------------

    if not st.session_state.generated:

        st.info(
            """
Your resume preview will appear here after clicking
**Generate Resume**.
"""
        )

    # ------------------------------------------------------
    # Show Generated Resume
    # ------------------------------------------------------

    else:

        st.components.v1.html(
            st.session_state.resume_html,
            height=900,
            scrolling=True
        )

        st.divider()

        st.download_button(
            label="📥 Download Resume PDF",
            data=st.session_state.resume_pdf,
            file_name="AI_ATS_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )    
import streamlit as st
import google.generativeai as genai


# PAGE CONFIG


st.set_page_config(
    page_title="AI ATS Resume Builder",
    page_icon="📄",
    layout="wide"
)


# CUSTOM CSS


st.markdown("""
<style>

.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
}

.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#0d6efd;
}

.sub-title{
    text-align:center;
    color:gray;
    margin-bottom:30px;
}

label{
    font-weight:600 !important;
}

.stButton>button{
    width:100%;
    border-radius:8px;
}

.resume{
    width:210mm;
    min-height:297mm;
    margin:auto;
    background:white;
    padding:45px;
    box-shadow:0px 0px 15px rgba(0,0,0,.15);
}

.section-title{
    font-size:20px;
    font-weight:bold;
    color:#0d6efd;
    border-bottom:2px solid #0d6efd;
    margin-top:20px;
    margin-bottom:8px;
}

.name{
    font-size:34px;
    font-weight:bold;
}

.contact{
    font-size:14px;
    color:#555;
}

.summary{
    text-align:justify;
    line-height:1.8;
}

</style>
""", unsafe_allow_html=True)


# SESSION STATE


defaults = {
    "skills": [],
    "education": [],
    "experience": [],
    "projects": [],
    "certifications": [],
    "languages": [],
    "achievements": []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value.copy()


# HELPER FUNCTIONS


def add_skill():
    st.session_state.skills.append("")


def add_education():
    st.session_state.education.append({
        "degree":"",
        "college":"",
        "university":"",
        "cgpa":"",
        "year":""
    })


def add_experience():
    st.session_state.experience.append({
        "company":"",
        "designation":"",
        "start_date":"",
        "end_date":"",
        "description":""
    })


def add_project():
    st.session_state.projects.append({
        "title":"",
        "description":""
    })


def add_certification():
    st.session_state.certifications.append("")


def add_language():
    st.session_state.languages.append("")


def add_achievement():
    st.session_state.achievements.append("")



# GEMINI SUMMARY FUNCTION


def generate_summary(candidate_information):

    prompt = f"""
You are a professional ATS Resume Writer.

Write ONLY one professional summary.

Rules:
- Maximum 80 words.
- ATS friendly.
- No bullet points.
- No headings.
- No repeated information.
- Professional tone.
- Mention skills naturally.
- Mention education.
- Mention projects.
- Mention work experience if available.
- If the candidate is a fresher, write accordingly.

Candidate Details:

{candidate_information}
"""

    try:

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:

        return f"Summary generation failed.\n\n{e}"



# PAGE TITLE


st.markdown(
    "<div class='main-title'>AI ATS Resume Builder</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub-title'>Generate Professional ATS Friendly Resume using AI</div>",
    unsafe_allow_html=True
)


# SIDEBAR


with st.sidebar:

    st.header("Gemini API")

    api_key = st.text_input(
        "Enter Gemini API Key",
        type="password"
    )

    if api_key:

        genai.configure(api_key=api_key)

        st.success("API Connected")

    else:

        st.info("Enter your Gemini API Key")


# MAIN LAYOUT


left, right = st.columns([1.2, 1])

with left:

    st.header("Personal Details")

    name = st.text_input("Full Name *")

    phone = st.text_input("Phone Number *")

    email = st.text_input("Email Address *")

    linkedin = st.text_input("LinkedIn")

    github = st.text_input("GitHub")

    portfolio = st.text_input("Portfolio")

    address = st.text_area("Address")

    
    # SKILLS
    

    st.divider()

    st.header("Skills")

    if st.button("➕ Add Skill"):

        add_skill()

    if len(st.session_state.skills) == 0:

        add_skill()

    skills = []

    for i in range(len(st.session_state.skills)):

        skill = st.text_input(
            f"Skill {i+1}",
            key=f"skill_{i}"
        )

        if skill.strip():

            skills.append(skill.strip())

    # Remove duplicate skills

    skills = list(dict.fromkeys(skills))

    
    # EDUCATION
    

    st.divider()

    st.header("Education")

    if st.button("➕ Add Education"):

        add_education()

    if len(st.session_state.education) == 0:

        add_education()

    education = []

    for i in range(len(st.session_state.education)):

        st.subheader(f"Education {i+1}")

        degree = st.text_input(
            "Degree",
            key=f"degree_{i}"
        )

        college = st.text_input(
            "College",
            key=f"college_{i}"
        )

        university = st.text_input(
            "University",
            key=f"university_{i}"
        )

        cgpa = st.text_input(
            "CGPA / Percentage",
            key=f"cgpa_{i}"
        )

        year = st.text_input(
            "Passing Year",
            key=f"year_{i}"
        )

        education.append({

            "degree": degree,

            "college": college,

            "university": university,

            "cgpa": cgpa,

            "year": year

        })

    
    # EXPERIENCE
    

    st.divider()

    fresher = st.checkbox("I am a Fresher")

    experience = []

    if not fresher:

        st.header("Experience")

        if st.button("➕ Add Experience"):

            add_experience()

        if len(st.session_state.experience) == 0:

            add_experience()

        for i in range(len(st.session_state.experience)):

            st.subheader(f"Experience {i+1}")

            company = st.text_input(
                "Company",
                key=f"company_{i}"
            )

            designation = st.text_input(
                "Designation",
                key=f"designation_{i}"
            )

            col1, col2 = st.columns(2)

            with col1:

                start_date = st.text_input(
                    "Start Date",
                    key=f"start_{i}"
                )

            with col2:

                end_date = st.text_input(
                    "End Date",
                    key=f"end_{i}"
                )

            description = st.text_area(
                "Responsibilities",
                key=f"description_{i}"
            )

            experience.append({

                "company": company,

                "designation": designation,

                "start_date": start_date,

                "end_date": end_date,

                "description": description

            })
        
    # PROJECTS
    

    st.divider()

    st.header("Projects")

    if st.button("➕ Add Project"):

        add_project()

    if len(st.session_state.projects) == 0:

        add_project()

    projects = []

    for i in range(len(st.session_state.projects)):

        st.subheader(f"Project {i+1}")

        title = st.text_input(
            "Project Title",
            key=f"project_title_{i}"
        )

        description = st.text_area(
            "Project Description",
            key=f"project_description_{i}"
        )

        projects.append({

            "title": title,

            "description": description

        })

    
    # CERTIFICATIONS
    

    st.divider()

    st.header("Certifications (Optional)")

    if st.button("➕ Add Certification"):

        add_certification()

    if len(st.session_state.certifications) == 0:

        add_certification()

    certifications = []

    for i in range(len(st.session_state.certifications)):

        cert = st.text_input(

            f"Certification {i+1}",

            key=f"certification_{i}"

        )

        if cert.strip():

            certifications.append(cert.strip())

    
    # LANGUAGES
    

    st.divider()

    st.header("Languages Known")

    if st.button("➕ Add Language"):

        add_language()

    if len(st.session_state.languages) == 0:

        add_language()

    languages = []

    for i in range(len(st.session_state.languages)):

        lang = st.text_input(

            f"Language {i+1}",

            key=f"language_{i}"

        )

        if lang.strip():

            languages.append(lang.strip())

    
    # ACHIEVEMENTS
    

    st.divider()

    st.header("Achievements (Optional)")

    if st.button("➕ Add Achievement"):

        add_achievement()

    if len(st.session_state.achievements) == 0:

        add_achievement()

    achievements = []

    for i in range(len(st.session_state.achievements)):

        achievement = st.text_input(

            f"Achievement {i+1}",

            key=f"achievement_{i}"

        )

        if achievement.strip():

            achievements.append(achievement.strip())

    
    # GENERATE RESUME BUTTON
    

    st.divider()

    generate_resume = st.button(

        "🚀 Generate Resume",

        use_container_width=True,

        type="primary"

    )            
        
    # GENERATE RESUME
    

    if generate_resume:

        #  Mandatory Validation  #

        if not name.strip():

            st.error("Full Name is required.")
            st.stop()

        if not phone.strip():

            st.error("Phone Number is required.")
            st.stop()

        if not email.strip():

            st.error("Email Address is required.")
            st.stop()

        if len(skills) == 0:

            st.error("Please add at least one skill.")
            st.stop()

        # Remove Empty Entries  #

        education = [
            edu for edu in education
            if edu["degree"].strip()
        ]

        projects = [
            project for project in projects
            if project["title"].strip()
        ]

        certifications = [
            cert for cert in certifications
            if cert.strip()
        ]

        languages = [
            lang for lang in languages
            if lang.strip()
        ]

        achievements = [
            achievement for achievement in achievements
            if achievement.strip()
        ]

        if not fresher:

            experience = [
                exp for exp in experience
                if exp["company"].strip()
            ]

        else:

            experience = []

        #  Prepare AI Prompt #

        candidate_information = f"""

Name:
{name}

Skills:
{", ".join(skills)}

Education:
{education}

Experience:
{experience}

Projects:
{projects}

Certifications:
{certifications}

Languages:
{languages}

Achievements:
{achievements}

"""

        # Generate prof. Summary #

        if api_key:

            with st.spinner("Generating AI Professional Summary..."):

                professional_summary = generate_summary(candidate_information)

        else:

            professional_summary = "API Key not provided. AI summary could not be generated."


# RIGHT COLUMN FOR RESUME PREVIEW


with right:

    st.header("Resume Preview")

    if generate_resume:

        st.success("Resume Generated Successfully!")

        st.markdown(
            f"""
<div class="resume">

<div class="name">{name}</div>

<div class="contact">

📞 {phone} &nbsp;&nbsp;&nbsp;

📧 {email}

</div>

""",
            unsafe_allow_html=True
        )

        if linkedin:

            st.markdown(
                f"**LinkedIn:** {linkedin}"
            )

        if github:

            st.markdown(
                f"**GitHub:** {github}"
            )

        if portfolio:

            st.markdown(
                f"**Portfolio:** {portfolio}"
            )

        if address:

            st.markdown(address)

        st.markdown(
            '<div class="section-title">Professional Summary</div>',
            unsafe_allow_html=True
        )

        st.write(professional_summary)

                
        # SKILLS
        

        st.markdown(
            '<div class="section-title">Skills</div>',
            unsafe_allow_html=True
        )

        st.write(" • ".join(skills))

        
        # EDUCATION
        

        if education:

            st.markdown(
                '<div class="section-title">Education</div>',
                unsafe_allow_html=True
            )

            for edu in education:

                st.markdown(
                    f"""
**{edu['degree']}**

{edu['college']}

{edu['university']}

CGPA / Percentage: {edu['cgpa']}

Year: {edu['year']}
"""
                )

        
        # EXPERIENCE
        

        if experience:

            st.markdown(
                '<div class="section-title">Experience</div>',
                unsafe_allow_html=True
            )

            for exp in experience:

                st.markdown(
                    f"""
### {exp['designation']}

**{exp['company']}**

{exp['start_date']} - {exp['end_date']}

{exp['description']}
"""
                )

        
        # PROJECTS
        

        if projects:

            st.markdown(
                '<div class="section-title">Projects</div>',
                unsafe_allow_html=True
            )

            for project in projects:

                st.markdown(
                    f"""
### {project['title']}

{project['description']}
"""
                )

        
        # CERTIFICATIONS
       

        if certifications:

            st.markdown(
                '<div class="section-title">Certifications</div>',
                unsafe_allow_html=True
            )

            for cert in certifications:

                st.write(f"• {cert}")

        
        # LANGUAGES
        

        if languages:

            st.markdown(
                '<div class="section-title">Languages</div>',
                unsafe_allow_html=True
            )

            st.write(", ".join(languages))

        
        # ACHIEVEMENTS
        

        if achievements:

            st.markdown(
                '<div class="section-title">Achievements</div>',
                unsafe_allow_html=True
            )

            for achievement in achievements:

                st.write(f"• {achievement}")

        st.markdown("</div>", unsafe_allow_html=True)

    else:

        st.info("Fill the form and click **Generate Resume** to preview your ATS-friendly resume.")
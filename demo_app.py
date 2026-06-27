import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Resume Builder")

name = st.text_input("Full Name")

education = st.text_area("Education")

skills = st.text_area("Skills")

projects = st.text_area("Projects")

experience = st.text_area("Experience")

if st.button("Generate Resume"):

    prompt = f"""
    Create a professional resume using the following details.

    Name: {name}

    Education:
    {education}

    Skills:
    {skills}

    Projects:
    {projects}

    Experience:
    {experience}

    Format the resume professionally with:
    - Professional Summary
    - Education
    - Skills
    - Projects
    - Experience
    """

    response = model.generate_content(prompt)

    st.subheader("Generated Resume")

    st.write(response.text)
# ============================================
# ai_summary.py
# Gemini Professional Summary Generator
# ============================================

import google.generativeai as genai


def generate_summary(resume_data, api_key):

    """
    Generates an ATS-friendly professional summary
    using Gemini.
    """

    if not api_key:

        return "API Key not provided. AI summary could not be generated."

    try:

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel("gemini-2.5-flash")

        prompt = f"""
You are an expert ATS Resume Writer.

Generate a professional resume summary.

Rules:

- Maximum 80 words.
- Professional tone.
- ATS Friendly.
- No bullet points.
- No repetition.
- Mention skills.
- Mention education.
- Mention experience if available.
- Mention projects if available.
- Write in third person.

Candidate Information:

{resume_data}
"""

        response = model.generate_content(prompt)

        return response.text.strip()

    except Exception as e:

        return f"Unable to generate summary.\n\n{str(e)}"
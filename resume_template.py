# ============================================
# resume_template.py
# Generates ATS Friendly Resume in HTML
# ============================================

from html import escape


def generate_resume_html(data):
    """
    Generates a professional ATS-friendly HTML resume.

    Parameters
    ----------
    data : dict
        Resume information collected from app.py

    Returns
    -------
    str
        HTML Resume
    """

    # -----------------------------
    # Personal Details
    # -----------------------------

    name = escape(data.get("name", ""))

    phone = escape(data.get("phone", ""))

    email = escape(data.get("email", ""))

    linkedin = escape(data.get("linkedin", ""))

    github = escape(data.get("github", ""))

    portfolio = escape(data.get("portfolio", ""))

    address = escape(data.get("address", ""))

    summary = escape(data.get("summary", ""))

    # -----------------------------
    # HTML START
    # -----------------------------

    html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>{name} Resume</title>

<style>

body{{
    font-family:Arial,Helvetica,sans-serif;
    background:#f3f3f3;
    margin:0;
    padding:0;
}}

.resume{{
    width:210mm;
    margin:auto;
    background:white;
    padding:30px;
    box-sizing:border-box;
}}

.name{{
    text-align:center;
    font-size:30px;
    font-weight:bold;
}}

.contact{{
    text-align:center;
    font-size:14px;
    margin-top:8px;
    color:#444;
}}

.section{{
    margin-top:12px;
    margin-bottom:8px;
}}

.section-title{{

    font-size:16px;
    font-weight:bold;
    border-bottom:1px solid black;

    margin:8px 0 6px 0;

    padding-bottom:2px;

}}

.text{{
    font-size:13px;
    line-height:1.2;
    text-align:left;
    margin:0;
}}

ul{{
    margin:4px 0;
    padding-left:18px;
}}

li{{
    margin:2px 0;
    padding:0;
}}

.item-title{{
    font-size:15px;
    font-weight:bold;
}}

.item-subtitle{{
    color:#555;
    font-size:13px;
}}

*{{
    margin:0;
    padding:0;
}}

</style>

</head>

<body>

<div class="resume">

<div class="name">
{name}
</div>

<div class="contact">

{phone} |
{email}
"""

    if linkedin:
        html += f" | {linkedin}"

    if github:
        html += f" | {github}"

    if portfolio:
        html += f" | {portfolio}"

    if address:
        html += f"<br>{address}"

    html += """
</div>
"""

    # -------------------------------------------------
    # PROFESSIONAL SUMMARY
    # -------------------------------------------------

    if summary:

        html += f"""
<div class="section">

<div class="section-title">
Professional Summary
</div>

<div class="text">
{summary}
</div>

</div>
"""

    # -------------------------------------------------
    # SKILLS
    # -------------------------------------------------

    skills = data.get("skills", [])

    if skills:

        html += """
<div class="section">

<div class="section-title">
Skills
</div>

<ul>
"""

        for skill in skills:

            html += f"<li>{escape(skill)}</li>"

        html += """
</ul>

</div>
"""

    # -------------------------------------------------
    # EXPERIENCE
    # -------------------------------------------------

    experience = data.get("experience", [])

    if experience:

        html += """
<div class="section">

<div class="section-title">
Experience
</div>
"""

        for exp in experience:

            start_date = f"{exp.get('start_month', '')} {exp.get('start_year', '')}".strip()

            if exp.get("currently_working"):
                end_date = "Present"
            else:
                end_date = f"{exp.get('end_month', '')} {exp.get('end_year', '')}".strip()

            html += f"""
<div class="item-title">
{escape(exp.get("designation",""))}
</div>

<div class="item-subtitle">
{escape(exp.get("company",""))}
</div>

<div class="item-subtitle">
{escape(start_date)} - {escape(end_date)}
</div>

<div class="text">
{escape(exp.get("responsibilities",""))}
</div>

<br>
"""

    # -------------------------------------------------
    # PROJECTS
    # -------------------------------------------------

    projects = data.get("projects", [])

    if projects:

        html += """
<div class="section">

<div class="section-title">
Projects
</div>
"""

        for project in projects:

            html += f"""
<div class="item-title">
{escape(project.get("title",""))}
</div>
"""

            if project.get("technology"):

                html += f"""
<div class="item-subtitle">
Technologies: {escape(project.get("technology",""))}
</div>
"""

            html += f"""
<div class="text">
{escape(project.get("description",""))}
</div>
"""

            if project.get("github"):

                html += f"""
<div class="item-subtitle">
GitHub:
{escape(project.get("github",""))}
</div>
"""

            if project.get("live_demo"):

                html += f"""
<div class="item-subtitle">
Live Demo:
{escape(project.get("live_demo",""))}
</div>
"""

            html += "<br>"

        html += """
</div>
"""
    # -------------------------------------------------
    # EDUCATION
    # -------------------------------------------------

    education = data.get("education", [])

    if education:

        html += """
<div class="section">

<div class="section-title">
Education
</div>
"""

        for edu in education:

            html += f"""
<div class="item-title">
{escape(edu.get("degree",""))}
</div>

<div class="item-subtitle">
{escape(edu.get("college",""))}
</div>
"""

            if edu.get("university"):

                html += f"""
<div class="item-subtitle">
{escape(edu.get("university",""))}
</div>
"""

            html += f"""
<div class="item-subtitle">
{escape(edu.get("cgpa",""))} {escape(edu.get("year",""))}
</div>

<br>
"""

        html += """
</div>
"""

    # -------------------------------------------------
    # CERTIFICATIONS
    # -------------------------------------------------

    certifications = data.get("certifications", [])

    if certifications:

        html += """
<div class="section">

<div class="section-title">
Certifications
</div>

<ul>
"""

        for cert in certifications:

            html += f"<li>{escape(cert)}</li>"

        html += """
</ul>

</div>
"""

    # -------------------------------------------------
    # LANGUAGES
    # -------------------------------------------------

    languages = data.get("languages", [])

    if languages:

        html += """
<div class="section">

<div class="section-title">
Languages
</div>

<ul>
"""

        for lang in languages:

            html += f"<li>{escape(lang)}</li>"

        html += """
</ul>

</div>
"""

    # -------------------------------------------------
    # ACHIEVEMENTS
    # -------------------------------------------------

    achievements = data.get("achievements", [])

    if achievements:

        html += """
<div class="section">

<div class="section-title">
Achievements
</div>

<ul>
"""

        for achievement in achievements:

            html += f"<li>{escape(achievement)}</li>"

        html += """
</ul>

</div>
"""

    # -------------------------------------------------
    # END OF RESUME
    # -------------------------------------------------

    html += """
</div>

</body>

</html>
"""

    return html
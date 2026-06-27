# ============================================
# pdf_generator.py
# Converts HTML Resume to PDF
# ============================================

from weasyprint import HTML


def generate_pdf(html_content):
    """
    Converts HTML content into PDF bytes.

    Parameters
    ----------
    html_content : str
        HTML generated from resume_template.py

    Returns
    -------
    bytes
        PDF file as bytes
    """

    try:

        pdf = HTML(string=html_content).write_pdf()

        return pdf

    except Exception as e:

        raise Exception(f"PDF Generation Failed: {str(e)}")
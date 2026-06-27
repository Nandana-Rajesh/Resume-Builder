# ============================================
# pdf_generator.py
# Converts HTML Resume to PDF
# ============================================

from io import BytesIO
from xhtml2pdf import pisa


def generate_pdf(html_content):
    """
    Converts HTML content into PDF bytes.
    """

    pdf = BytesIO()

    result = pisa.CreatePDF(
        src=html_content,
        dest=pdf
    )

    if result.err:
        raise Exception("PDF generation failed.")

    return pdf.getvalue()
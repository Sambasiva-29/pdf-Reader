from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def generate_pdf(file_name, details):
    pdf_path = f"output/reports/{file_name}.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A4)

    y = 800
    for key, value in details.items():
        c.drawString(40, y, f"{key}: {value}")
        y -= 20

    c.save()


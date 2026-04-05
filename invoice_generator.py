import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_invoice(data):
    print("MASUK GENERATE")  # DEBUG

    os.makedirs("output", exist_ok=True)

    file_name = "output/test_invoice.pdf"  # SENGAJA STATIC DULU
    c = canvas.Canvas(file_name, pagesize=letter)

    c.drawString(100, 750, "INVOICE TEST")
    c.drawString(100, 700, f"Client: {data['client']}")
    c.drawString(100, 650, f"Total: Rp {data['total']}")

    c.save()

    print("PDF BERHASIL DIBUAT")
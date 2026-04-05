from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def generate_invoice(data):
    file_name = f"output/invoice_{data['client']}.pdf"
    c = canvas.Canvas(file_name, pagesize=letter)

    #judul
    c.setFont("Arial, 16")
    c.drawString(200, 750, "INVOICE")

    #info
    c.setFont("Arial", 12)
    c.drawString(50, 700, f"Client: {data['client']}")
    c.drawString(50, 680, f"Tanggal: {data['date']}")

    #table
    y = 640
    for item in data ['items']:
        c.drawString(50, y, item['nama'])
        c.drawString(250, y, str(item['qty']))
        c.drawString(300, y, str(item['harga']))
        c.drawString(400, y, str(item['subtotal']))
        y -= 20

    #total
    c.drawString(50, y - 20, f"Total: Rp {data['Total']}")

    c.save()
    print("Invoice berhasil dibuat!")
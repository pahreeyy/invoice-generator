import data_handler
import invoice_generator

print("IMPORT AMAN")

data = {
    "client": "TEST",
    "date": "01-01-2025",
    "items": [],
    "total": 10000
}

invoice_generator.generate_invoice(data)

print("SELESAI")
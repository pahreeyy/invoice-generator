from invoice_generator import generate_invoice
from data_handler import get_input_data

print("Mulai input...")

data = get_input_data()

print("Data:", data)

try:
    generate_invoice(data)
    print("Selesai generate")
except Exception as e:
    print("ERROR TERJADI:", e)
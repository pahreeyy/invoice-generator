from invoice_generator import generate_invoice
from data_handler import get_input_data

data = get_input_data()
generate_invoice(data)

print("Mulai input...")
data = get_input_data()

print("Datas sudah masuk:", data)

generate_invoice(data)

print("Selesai generate")
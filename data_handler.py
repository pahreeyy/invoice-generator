from datetime import datetime

def input_angka(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input harus angka! coba lagi.")

def get_input_data():
    # Validasi nama client
    while True:
        client_name = input("Nama Client: ")
        if client_name.strip() != "":
            break
        print("Nama client tidak boleh kosong!")

    date = datetime.now().strftime("%d-%m-%Y")

    items = []
    total = 0

    # Input item (loop manual)
    while True:
        print("\n--- Tambah Item ---")
        nama = input("Nama unit: ")
        qty = input_angka("Qty: ")
        harga = input_angka("Harga: ")

        subtotal = qty * harga
        total += subtotal

        items.append({
            "nama": nama,
            "qty": qty,
            "harga": harga,
            "subtotal": subtotal
        })

        # Tanya lanjut atau tidak
        lagi = input("Tambah item lagi? (y/n): ")
        if lagi.lower() != 'y':
            break

    return {
        "client": client_name,
        "date": date,
        "items": items,
        "total": total
    }
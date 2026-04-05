from datetime import datetime

def get_input_data():
    client_name = input("Nama Client: ")
    date = datetime.now().strftime("%d-%m-%y")

    items = []
    total = 0

    jumlah_item = int(input("Jumlah item: "))

    for i in range(jumlah_item):
        nama = input("Nama unit: ")
        qty = int(input("Qty: "))
        harga = int(input("Harga: "))

        subtotal = qty * harga
        total += subtotal

        items.append({
            "nama": nama,
            "qty": qty,
            "harga": harga,
            "subtotal": subtotal
        })

    return {
        "client": client_name,
        "date": date,
        "items": items,
        "total": total
    }
import json

while True:
    print("\n====== MENU ======")
    print("1. Lihat data")
    print("2. Tambah data")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        with open("ddp6.json", "r", encoding = "utf-8") as f :
            data = json.load(f)
        print("\nData yang telah tersimpan:")
        for item in data:
            print("Nama:", item["nama"])
            print("Harga:", item["harga"])
            print("Stok:", item["stok"])

    if pilihan == "2":
        nama = input("Masukkan nama produk: ")
        harga = input("Masukkan harga produk: ")
        stok = input("Masukkan stok produk: ")
        with open("ddp6.json", "r", encoding = "utf-8") as f :
            data = json.load(f)

        data.append({
            "nama": nama,
            "harga": harga,
            "stok": stok
        })

        with open("ddp6.json", "w", encoding = "utf-8") as f :
            json.dump(data, f, indent = 4)

        print("\nData berhasil ditambahkan!")

    if pilihan == "3":
        print("Terima kasih telah menggunakan program ini.")
        break
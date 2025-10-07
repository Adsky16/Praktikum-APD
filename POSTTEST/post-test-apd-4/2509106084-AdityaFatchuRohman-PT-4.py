#data login
nama = "AdityaFR"
nim = "2509106084"

#validasi login maks. 3
percobaan = 0

while percobaan < 3:
    print("\n=== Login ===")
    username = input("Masukkan username: ")
    password = input("Masukkan Password: ")

    if username == nama and password == nim:
        print(f"\nLogin berhasil!, selamat datang {nama}")
        break
    else:
        percobaan += 1
        print(f"\nLogin gagal! Anda memiliki {3-percobaan} percobaan lagi.")

if percobaan == 3:
    print("\nAnda telah mencapai batas percobaan login. Program dihentikan.")

else:
    total_reguler = 0
    total_vip = 0
    total_vvip = 0
    jumlah_reguler = 0
    jumlah_vip = 0
    jumlah_vvip = 0

#menu pemnelian tiket
    while True:
        print("\n=== Menu Pembelian Tiket XX0 ===")
        print("1. Tiket Reguler (Rp 50.000)")
        print("2. Tiket VIP (Rp 100.000)")
        print("3. Tiket VVIP (Rp 150.000)")
        print("4. Keluar dan Tampilkan Struk")
        opsi = input("\nPilih opsi (1-4): ")

        if opsi == "4":
            total_bayar = total_reguler + total_vip + total_vvip
            print("\n==== Struk Pembelian Tiket XX0 ====")
            print(f"Tiket Reguler: {jumlah_reguler} tiket, Total: Rp.{total_reguler}")
            print(f"Tiket VIP    : {jumlah_vip} tiket, Total: Rp.{total_vip}")
            print(f"Tiket VVIP   : {jumlah_vvip} tiket, Total: Rp.{total_vvip}")
            print("---------------------------------------")
            print(f"Total Pembelian              : Rp.{total_bayar}")
#diskon
            potongan = 0
            bonus = ""

            if total_bayar >= 300000:
                potongan = total_bayar * 0.12
            elif total_bayar >= 200000:
                potongan = total_bayar * 0.08
            elif total_bayar >= 150000:
                bonus = "Poster Film Eksklusif"

            total_akhir = total_bayar - potongan

            if potongan > 0:
                print(f"Potongan Harga               : Rp.{potongan}")
            if bonus != "":
                print(f"Bonus                        : {bonus}")
            print(f"---------------------------------------")
            print(f"Total Harga                  : Rp.{total_akhir}")
            print("\nTerima kasih telah membeli tiket di XX0!")
            exit()

        elif opsi == "1":
            jumlah = int(input("Masukkan jumlah tiket Reguler yang ingin dibeli: "))
            harga = 50000
            for i in range(jumlah):
                total_reguler += harga
            jumlah_reguler += jumlah
            print(f"\n{jumlah} tiket Reguler berhasil ditambahkan ke keranjang.")

        elif opsi == "2":
            jumlah = int(input("Masukkan jumlah tiket VIP yang ingin dibeli: "))
            harga = 100000
            for i in range(jumlah):
                total_vip += harga
            jumlah_vip += jumlah
            print(f"\n{jumlah} tiket VIP berhasil ditambahkan ke keranjang.")

        elif opsi == "3":
            jumlah = int(input("Masukkan jumlah tiket VVIP yang ingin dibeli: "))
            harga = 150000
            for i in range(jumlah):
                total_vvip += harga
            jumlah_vvip += jumlah
            print(f"\n{jumlah} tiket VVIP berhasil ditambahkan ke keranjang.")

        else:
            print("Opsi tidak valid. Silakan pilih opsi 1-4.")
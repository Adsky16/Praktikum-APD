#key login
key_nama = "Aditya Fatchu Rohman"
key_nim = "2509106084"

biaya_langganan = 1500000

print("\n=== Selamat datang di program langganan streaming musik ===")

#input login
nama = input("\nMasukkan nama Anda : ")
nim = input("Masukkan NIM Anda : ")

#percabangan
if nama == key_nama and nim == key_nim:
    print(f"\nSelamat datang, {nama}!")
    print(f"\nBiaya langganan bulanan Anda adalah Rp.{biaya_langganan}")
    print("Pilih paket langganan :")
    print("1. Bronze (admin 1%)")
    print("2. Silver (admin 3%)")
    print("3. Gold (admin 5%)")
    print("4. Platinum (admin 7%)")

    pilihan = input("\nMasukkan pilihan paket langganan Anda (1/2/3/4) : ")
    if pilihan == "1":
        admin = 0.01
        total_bayar = biaya_langganan + (biaya_langganan * admin)
        print(f"\n=== Paket Bronze ===")
        print("Benefit : Akses dasar ke lagu-lagu populer")
        print(f"Total bayar : Rp. {total_bayar}")
    elif pilihan == "2":
        admin = 0.03
        total_bayar = biaya_langganan + (biaya_langganan * admin)
        print(f"\n=== Paket Silver ===")
        print("Benefit : Akses ke lagu-lagu premium dan playlist custom")
        print(f"Total bayar : Rp. {total_bayar}")
    elif pilihan == "3":
        admin = 0.05
        total_bayar = biaya_langganan + (biaya_langganan * admin)
        print(f"\n=== Paket Gold ===")
        print("Benefit : Akses ke lagu-lagu premium, playlist custom, dan mode offline")
        print(f"Total bayar : Rp. {total_bayar}")
    elif pilihan == "4":
        admin = 0.07
        total_bayar = biaya_langganan + (biaya_langganan * admin)
        print(f"\n=== Paket Platinum ===")
        print("Benefit : Semua fitur, playlist custom, mode offline dan konten eksklusif artis")
        print(f"Total bayar : Rp. {total_bayar}")
    else:
        print("\nPilihan paket langganan tidak valid.")
else:
    print("\nNama atau NIM yang Anda masukkan salah. Akses ditolak.")
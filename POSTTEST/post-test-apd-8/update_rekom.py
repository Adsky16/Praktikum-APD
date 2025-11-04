from fungsi import clear, pause
from data import jenis_senjata, model_senjata, rekomendasi_list

def update_rekomendasi():
    while True:
        clear()
        print("=== UPDATE REKOMENDASI SENJATA ===")
        print("1. Tambah Rekomendasi")
        print("2. Hapus Rekomendasi")
        print("3. Kembali")
        pilih = input("Pilih opsi: ")

        if pilih == '1':
            clear()
            print("=== JENIS SENJATA TERSEDIA ===")
            for i in range(len(jenis_senjata)):
                print(f"{i+1}. {jenis_senjata[i]}")
            try:
                jenis = int(input("Pilih jenis senjata: ")) - 1
                if jenis < len(jenis_senjata):
                    clear()
                    print("=== DAFTAR MODEL " + jenis_senjata[jenis].upper() + " YANG TERSEDIA ===")
                    for i in range(len(model_senjata[jenis])):
                        print(str(i+1) + ". " + model_senjata[jenis][i])

                    print("\n--- REKOMENDASI SAAT INI ---")
                    for i in range(len(rekomendasi_list[jenis])):
                        print("- " + rekomendasi_list[jenis][i])

                    nama = input("Masukkan nama model yang ingin direkomendasikan: ").upper()
                    if nama in model_senjata[jenis]:
                        rekomendasi_list[jenis].append(nama)
                        print("Model berhasil ditambahkan ke rekomendasi!")
                    else:
                        print("Model tidak ditemukan di daftar senjata.")
                else:
                    print("Jenis tidak valid!")
            except ValueError:
                print("Input harus angka!")
            pause()

        elif pilih == '2':
            clear()
            print('=== DAFTAR JENIS SENJATA ===')
            for i in range(len(jenis_senjata)):
                print(f"{i+1}. {jenis_senjata[i]}")
            try:
                jenis = int(input("Pilih jenis senjata: ")) - 1
                if jenis < len(jenis_senjata):
                    clear()
                    print(f"=== Daftar Rekomendasi {jenis_senjata[jenis]} ===")
                    for k in range(len(rekomendasi_list[jenis])):
                        print(f"{k+1}. {rekomendasi_list[jenis][k]}")
                    hapus = int(input("Pilih nomor yang ingin dihapus: ")) - 1
                    if hapus < len(rekomendasi_list[jenis]):
                        del rekomendasi_list[jenis][hapus]
                        print("Rekomendasi berhasil dihapus!")
                    else:
                        print("Nomor tidak valid!")
                else:
                    print("Jenis tidak valid!")
            except ValueError:
                print("Input harus angka!")
            pause()

        elif pilih == '3':
            break
        else:
            print("Pilihan tidak valid!")
            pause()
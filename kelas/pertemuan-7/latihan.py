def menu():
    print("=== Menu ===")
    print("1. Tampilkan data")
    print("2. Tambah data")
    print("3. Ubah data")
    print("4. Hapus data")
    print("5. Keluar")
    pilih = input("Pilih menu (1-5): ")
    return pilih

def tambah_data():
    print("Menambahkan data...")
    print("Data berhasil ditambahkan.")

def tampilkan_data():
    print("Menampilkan data...")
    print("Data ditampilkan.")

def tampilkan_data():
    print("Menampilkan data...")
    print("Data ditampilkan.")

def ubah_data():
    print("Mengubah data...")
    print("Data berhasil diubah.")

def hapus_data():
    print("Menghapus data...")
    print("Data berhasil dihapus.")    

while True:
    pilihan = menu()
    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampilkan_data()
    elif pilihan == "3":
        ubah_data()
    elif pilihan == "4":
        hapus_data()
    else:
        print("Pilihan tidak valid")







# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print ("luas persegi panjang adalah", luas)

# luas_persegi_panjang(4, 5)

# nama = "Ridho"

# def salam():
#     nama = "andi"
#     print("halo", nama)

# print(nama)
# salam()


# try:
#     angka = int(input("Masukkan nomor: "))
# except ValueError:
#     print('Kamu gak masukin angka')
# else:
#     print('kamu ketik', angka)
# finally:
#     print('Selesai')

try:
    pw = input('Masukkan PW: ')
    if len(pw) > 8:
        raise print('kebanyakan')
except ValueError as i:
    print(1)
else:
    print('LOGIN')
finally:
    print('lnjt')
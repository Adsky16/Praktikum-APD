print("\nSelamat datang di restoran kami!")
print("Silahkan tulis nama, NIM, dan harga menu yang Anda pilih.")

#Input konsumen
nama = input("\nMasukkan Nama : ")
nim = input("Masukkan NIM  : ")
harga = int(input("Masukkan harga (Rp): "))

#pajak setiap menu
pajak_PL = harga * (5/100)
pajak_MA = harga * (8/100)
pajak_NP = harga * (10/100)

#menghitung total harga setiap menu
total_PL = harga + pajak_PL
total_MA = harga + pajak_MA
total_NP = harga + pajak_NP

#output
print("\n--- STRUK PEMBAYARAN ---")
print(f"Nama Konsumen  : {nama}")
print(f"NIM Konsumen   : {nim}")
print(f"Harga Menu Awal: Rp. {harga}")
print("\nDaftar Harga Setelah Pajak:")
print("=======================================")
print("|   Menu     |Pajak (%)|   Total Harga|")
print("=======================================")
print(f"|Pecel lele  |   5%    |   Rp. {total_PL}|")
print(f"|Mie ayam    |   8%    |   Rp. {total_MA}|")
print(f"|Nasi padang |  10%    |   Rp. {total_NP}|")   
print("=======================================")
print("Terima kasih telah berkunjung!") 
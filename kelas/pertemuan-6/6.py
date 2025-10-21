# buah = {"apel", "jeruk", "mangga", "apel"}
# print(buah)

# angka_ganjil = {1, 3, 5, 7, 9}

# angka_ganjil.add(15)
# angka_ganjil.discard(5)

# for angka in angka_ganjil:
#     print(angka)

# Daftar_buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }
# print(Daftar_buku["Buku1"])
# print(Daftar_buku)
# print(Daftar_buku.keys())

# for key in Daftar_buku.keys():
#     print(key)

# for value in Daftar_buku.values():
#     print(value)

# for A in Daftar_buku.items():
#     print(A)

# Biodata = {
#     "Nama" : "Ananda Daffa Harahap",
#     "NIM" : 2409106050,
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data", "Algoritma", "Jaringan Komputer"],
#     "Mahasiswa_Aktif" : True,
#     "Social Media" : {"Instagram" : "daffahrhap"}
# }

# for A,J in Biodata.items():
#     print(f"{A} : {J}")

# list_mahasiswa = dict(nama="dapupu", jurusan="Informatika")
# print(list_mahasiswa)

# print(f"nama saya adalah {Biodata["Nama"]}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"\nnama saya adalah {Biodata.get("Nama")}")
# print(Biodata.get("KRS")[1:3])

# Nilai = {
#     "Matematika": 80,
#     "B. Indonesia": 90,
#     "B. Inggris": 81,
#     "Kimia": 78,
#     "Fisika": 80
#     }
# # Tanpa menggunakan items()
# for i in Nilai:
#     print(i)
# print("") # pemisah
# # Menggunakan items()
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# #Sebelum Diubah
# print(Film)
# Film["Sherlock Holmes"] = "Action"
# Film.update({"The Conjuring" : "Tragedy"})
# #Sesudah Diubah
# print(Film)
#nilai = int(input("Masukkan nilai: "))
#
#if nilai >= 80:
#    print("A")
#elif nilai >= 70:
#    print("B")
#elif nilai >= 60:
#    print("C")
#elif nilai == 100:
#    print("A+")
#else:
#    print("Tidak lulus")

belanja = int(input("Masukkan jumlah belanja: "))   
if belanja > 100000:
    print("Selamat, Anda mendapatkan diskon 20%")
elif belanja > 50000:
    print("Selamat, Anda mendapatkan diskon 10%")
else:
    print("Maaf, Anda tidak mendapatkan diskon")
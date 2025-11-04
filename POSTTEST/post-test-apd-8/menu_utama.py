from fungsi import clear

def menu_utama(status):
    clear()
    print('=== DELTA FORCE ARMORY ===')
    print("1. Rekomendasi Senjata")
    if status == "admin":
        print("2. Update Rekomendasi Senjata")
        print("3. Kelola Model & Statistik Senjata")
        print("4. Keluar")
    else:
        print("2. Keluar")
    pilih = input("Pilih menu: ")
    return pilih
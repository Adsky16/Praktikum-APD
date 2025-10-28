import os
import sys


jenis_senjata = (
    "Rifle", "SMG", "Shotgun", "LMG", "Marksman Rifle",
    "Sniper Rifle", "Pistol", "Senjata Khusus"
)

model_senjata = [
    ["M4A1", "AKM", "K416", "M7", "SG552", 'AK-12', 'SCAR-H', 'PTR-32', 'AS VAL', 'CI-19', 'K437', 'KC17'],  # Rifle
    ['MP5', 'P90', 'VECTOR', 'UZI', 'BIZON', 'SMG-45', 'SR-3M', 'VITYAZ', 'QCQ171', 'MP7'],  # SMG
    ['M1014', 'S12K', 'M870', '725 DOUBLE'],  # Shotgun
    ['PKM', 'M249', 'M250', 'QCB-201'],  # LMG
    ['MINI-14', 'VSS', 'SVD', 'M14', 'SKS', 'SR-25', 'SR-9', 'PSG-1', 'MARLIN LEVER'],  # Marksman
    ['SV-98', 'R93', 'M700', 'AWM'],  # Sniper
    ['M1911', 'DESERT EAGLE', 'QSZ-92G', 'G18', '93R', '357 REVOLVER'],  # Pistol
    ['COMPOUND BOW']  # Senjata Khusus
]

# Statistik setiap jenis
statistik_rifle = [
    {"Damage": 42, "Fire Rate": 750, "Accuracy": 70, "Mobility": 60, "Range": 60},
    {"Damage": 49, "Fire Rate": 600, "Accuracy": 65, "Mobility": 55, "Range": 55},
    {"Damage": 45, "Fire Rate": 700, "Accuracy": 68, "Mobility": 58, "Range": 58},
    {"Damage": 44, "Fire Rate": 720, "Accuracy": 69, "Mobility": 59, "Range": 59},
    {"Damage": 46, "Fire Rate": 680, "Accuracy": 67, "Mobility": 57, "Range": 57},
    {"Damage": 47, "Fire Rate": 660, "Accuracy": 66, "Mobility": 56, "Range": 56},
    {"Damage": 48, "Fire Rate": 640, "Accuracy": 64, "Mobility": 54, "Range": 54},
    {"Damage": 50, "Fire Rate": 620, "Accuracy": 63, "Mobility": 53, "Range": 53},
    {"Damage": 43, "Fire Rate": 730, "Accuracy": 71, "Mobility": 61, "Range": 61},
    {"Damage": 41, "Fire Rate": 760, "Accuracy": 72, "Mobility": 62, "Range": 62},
    {"Damage": 44, "Fire Rate": 710, "Accuracy": 68, "Mobility": 59, "Range": 59},
    {"Damage": 45, "Fire Rate": 700, "Accuracy": 67, "Mobility": 58, "Range": 58},
]

statistik_smg = [
    {"Damage": 30, "Fire Rate": 900, "Accuracy": 60, "Mobility": 80, "Range": 30},
    {"Damage": 28, "Fire Rate": 950, "Accuracy": 58, "Mobility": 82, "Range": 28},
    {"Damage": 32, "Fire Rate": 850, "Accuracy": 62, "Mobility": 78, "Range": 32},
    {"Damage": 29, "Fire Rate": 920, "Accuracy": 59, "Mobility": 81, "Range": 29},
    {"Damage": 27, "Fire Rate": 970, "Accuracy": 57, "Mobility": 83, "Range": 27},
    {"Damage": 31, "Fire Rate": 880, "Accuracy": 61, "Mobility": 79, "Range": 31},
    {"Damage": 33, "Fire Rate": 840, "Accuracy": 63, "Mobility": 77, "Range": 33},
    {"Damage": 26, "Fire Rate": 980, "Accuracy": 56, "Mobility": 84, "Range": 26},
    {"Damage": 34, "Fire Rate": 830, "Accuracy": 64, "Mobility": 76, "Range": 34},
    {"Damage": 25, "Fire Rate": 990, "Accuracy": 55, "Mobility": 85, "Range": 25},
]

statistik_shotgun = [
    {"Damage": 70, "Fire Rate": 300, "Accuracy": 50, "Mobility": 40, "Range": 10},
    {"Damage": 75, "Fire Rate": 280, "Accuracy": 48, "Mobility": 38, "Range": 90},
    {"Damage": 80, "Fire Rate": 260, "Accuracy": 46, "Mobility": 36, "Range": 80},
    {"Damage": 85, "Fire Rate": 240, "Accuracy": 44, "Mobility": 34, "Range": 70},
]

statistik_lmg = [
    {"Damage": 55, "Fire Rate": 600, "Accuracy": 60, "Mobility": 50, "Range": 40},
    {"Damage": 50, "Fire Rate": 650, "Accuracy": 58, "Mobility": 52, "Range": 38},
    {"Damage": 52, "Fire Rate": 620, "Accuracy": 59, "Mobility": 51, "Range": 39},
    {"Damage": 54, "Fire Rate": 610, "Accuracy": 57, "Mobility": 53, "Range": 37},
]

statistik_marksman = [
    {"Damage": 60, "Fire Rate": 500, "Accuracy": 75, "Mobility": 45, "Range": 50},
    {"Damage": 58, "Fire Rate": 520, "Accuracy": 77, "Mobility": 44, "Range": 52},
    {"Damage": 65, "Fire Rate": 480, "Accuracy": 80, "Mobility": 43, "Range": 55},
    {"Damage": 62, "Fire Rate": 510, "Accuracy": 76, "Mobility": 46, "Range": 51},
    {"Damage": 59, "Fire Rate": 530, "Accuracy": 78, "Mobility": 44, "Range": 53},
    {"Damage": 64, "Fire Rate": 490, "Accuracy": 79, "Mobility": 45, "Range": 54},
    {"Damage": 61, "Fire Rate": 505, "Accuracy": 74, "Mobility": 46, "Range": 55},
    {"Damage": 66, "Fire Rate": 475, "Accuracy": 81, "Mobility": 42, "Range": 56},
    {"Damage": 63, "Fire Rate": 495, "Accuracy": 73, "Mobility": 47, "Range": 49},
]

statistik_sniper = [
    {"Damage": 90, "Fire Rate": 200, "Accuracy": 90, "Mobility": 30, "Range": 80},
    {"Damage": 95, "Fire Rate": 180, "Accuracy": 92, "Mobility": 28, "Range": 85},
    {"Damage": 100, "Fire Rate": 160, "Accuracy": 94, "Mobility": 27, "Range": 90},
    {"Damage": 110, "Fire Rate": 150, "Accuracy": 95, "Mobility": 25, "Range": 95},
]

statistik_pistol = [
    {"Damage": 35, "Fire Rate": 400, "Accuracy": 65, "Mobility": 70, "Range": 20},
    {"Damage": 45, "Fire Rate": 350, "Accuracy": 60, "Mobility": 68, "Range": 18},
    {"Damage": 33, "Fire Rate": 420, "Accuracy": 66, "Mobility": 72, "Range": 21},
    {"Damage": 30, "Fire Rate": 450, "Accuracy": 67, "Mobility": 73, "Range": 22},
    {"Damage": 28, "Fire Rate": 480, "Accuracy": 68, "Mobility": 74, "Range": 23},
    {"Damage": 50, "Fire Rate": 300, "Accuracy": 55, "Mobility": 65, "Range": 17},
]

statistik_khusus = [
    {"Damage": 25, "Fire Rate": 100, "Accuracy": 85, "Mobility": 90, "Range": 15},
]

semua_statistik = [statistik_rifle, statistik_smg, statistik_shotgun, statistik_lmg, statistik_marksman, statistik_sniper, statistik_pistol, statistik_khusus]


# Rekomendasi
rekomendasi_list = [
    ['M4A1', 'AKM', 'K416'],
    ['MP5', 'P90', 'VECTOR'],
    ['M1014', 'S12K'],
    ['PKM', 'M249'],
    ['MINI-14', 'VSS'],
    ['SV-98', 'R93'],
    ['M1911', 'DESERT EAGLE'],
    ['COMPOUND BOW']
]

data_user = [
    ["Aditya", "2202", "admin"],
    ["ForReal", "1608", "user"]
]


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def keluar():
    print("Terima kasih dan sampai jumpa!")
    sys.exit()

def pause():
    input('\nEnter untuk lanjut')

def login(username, password):
    for user in data_user:
        if user[0] == username and user[1] == password:
            return user[2]
    return ""

def menu_login():
    clear()
    print('=== LOGIN DELTA FORCE ARMORY ===')
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih menu (1-3): ")
    return pilih

def ulang_login():
    clear()
    username = input("Username: ")
    password = input("Password: ")
    status = login(username, password)
    if status == "":
        print("Username atau password salah! Coba lagi.\n")
        pause()
        return ulang_login()
    else:
        print(f"Berhasil login sebagai {status.upper()}!")
        pause()
        return status

def register():
    clear()
    print('=== REGISTER AKUN ===')
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    for user in data_user:
        if user[0] == username:
            print("Username sudah digunakan, gantii!")
            pause()
            return
    data_user.append([username, password, "user"])
    print("Akun berhasil dibuat!")
    pause()

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

def tampil_rekomendasi():
    while True:
        clear()
        print('=== REKOMENDASI SENJATA ===')
        for i in range(len(jenis_senjata)):
            print(f"{i+1}. {jenis_senjata[i]}")
        print(str(len(jenis_senjata)+1)+". Kembali")
        try:
            pilih = int(input("Pilih jenis (1-8): ")) - 1
            if pilih < len(jenis_senjata):
                tampil_model_rekomendasi(pilih)
            elif pilih == len(jenis_senjata):
                break
            else:
                print("Pilihan tidak valid!")
                pause()
        except ValueError:
            print("Input harus angka!")
            pause()

def tampil_model_rekomendasi(pilih_jenis):
    while True:
        clear()
        print("REKOMENDASI " + jenis_senjata[pilih_jenis]+":")
        for j in range(len(rekomendasi_list[pilih_jenis])):
            print(f"{j+1}. {rekomendasi_list[pilih_jenis][j]}")
        print(str(len(rekomendasi_list[pilih_jenis])+1) + ". Kembali")
        try:
            pilih_model = int(input("Pilih model untuk lihat statistik: ")) - 1
            if pilih_model < len(rekomendasi_list[pilih_jenis]):
                tampil_statistik(pilih_jenis, pilih_model)
            elif pilih_model == len(rekomendasi_list[pilih_jenis]):
                break
            else:
                print("Pilihan tidak valid!")
        except ValueError:
            print("Input harus angka!")
        pause()

def tampil_statistik(jenis, model):
    clear()
    print("=== STATISTIK SENJATA " + rekomendasi_list[jenis][model]+" ===")
    stats = semua_statistik[jenis][model]
    for k, v in stats.items():
        print(f"{k:10}: {v}")

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

def update_statistik():
    global semua_statistik, model_senjata
    while True:
        clear()
        print("=== UPDATE STATISTIK SENJATA (BUFF/NERF) ===")
        for i in range(len(jenis_senjata)):
            print(f"{i+1}. {jenis_senjata[i]}")
        print(str(len(jenis_senjata)+1)+". Kembali")
        try:
            jenis = int(input("Pilih jenis senjata: ")) - 1
            if jenis < len(jenis_senjata):
                while True:
                    clear()
                    print(f"=== UPDATE STATISTIK {jenis_senjata[jenis]} ===")
                    for j in range(len(model_senjata[jenis])):
                        print(f"{j+1}. {model_senjata[jenis][j]}")
                    print(str(len(model_senjata[jenis])+1) + ". Kembali")

                    pilih_model = int(input("Pilih model: ")) - 1
                    if pilih_model < len(model_senjata[jenis]):
                        try:
                            dmg = int(input("Damage baru   : "))
                            rate = int(input("Fire Rate baru: "))
                            acc = int(input("Accuracy baru : "))
                            mob = int(input("Mobility baru : "))
                            rng = int(input("Range baru    : "))
                            semua_statistik[jenis][pilih_model] = {
                                "Damage": dmg,
                                "Fire Rate": rate,
                                "Accuracy": acc,
                                "Mobility": mob,
                                "Range": rng
                            }
                            print("Statistik berhasil diperbarui!")
                            pause()
                        except ValueError:
                            print("Input harus berupa angka!")
                            pause()
                    elif pilih_model == len(model_senjata[jenis]):
                        break  
                    else:
                        print("Pilihan tidak valid!")
                        pause()
            elif jenis == len(jenis_senjata):
                break  
            else:
                print("Jenis tidak valid!")
                pause()
        except ValueError:
            print("Input harus berupa angka!")
            pause()

def tambah_model():
    global model_senjata, semua_statistik
    while True:
        clear()
        print("=== TAMBAH MODEL + STATISTIK ===")
        for i in range(len(jenis_senjata)):
            print(f"{i+1}. {jenis_senjata[i]}")
        print(str(len(jenis_senjata)+1)+'. Kembali')
        try:
            jenis = int(input("Pilih jenis: ")) - 1
            if jenis < len(jenis_senjata):
                clear()
                print(f"=== TAMBAH MODEL BARU UNTUK {jenis_senjata[jenis].upper()} ===")
                nama = input("Nama senjata baru: ").upper()
                try:
                    dmg = int(input("Damage   : "))
                    rate = int(input("Fire Rate: "))
                    acc = int(input("Accuracy : "))
                    mob = int(input("Mobility : "))
                    rng = int(input("Range    : "))
                    model_senjata[jenis].append(nama)
                    semua_statistik[jenis].append({
                        "Damage": dmg,
                        "Fire Rate": rate,
                        "Accuracy": acc,
                        "Mobility": mob,
                        "Range": rng
                    })
                    print("Model & statistik baru berhasil ditambahkan!")
                    pause()
                except ValueError:
                    print("Input harus berupa angka!")
                    pause()
            elif jenis == len(jenis_senjata):
                break
            else:
                print("Jenis tidak valid!")
                pause()
        except ValueError:
            print("Input harus angka!")
            pause()

def hapus_model():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== HAPUS MODEL & STATISTIK ===")
    for i in range(len(jenis_senjata)):
        print(str(i+1)+". "+jenis_senjata[i])
    print(str(len(jenis_senjata)+1)+". Kembali")
    try:
        jenis = int(input("Pilih jenis: ")) - 1
        if jenis == len(jenis_senjata):
            return  # kembali ke menu admin
        elif jenis < len(jenis_senjata):
            for j in range(len(model_senjata[jenis])):
                print(str(j+1)+". "+model_senjata[jenis][j])
            hapus = int(input("Pilih yang dihapus: ")) - 1
            if hapus < len(model_senjata[jenis]):
                dihapus = model_senjata[jenis].pop(hapus)
                semua_statistik[jenis].pop(hapus)
                print(f"Model & statistik '{dihapus}' berhasil dihapus!")
            else:
                print("Nomor tidak valid!")
        else:
            print("Pilihan tidak valid!")
    except ValueError:
        print("Input harus angka!")
    input("Enter untuk lanjut")

def kelola_model_statistik():
    while True:
        clear()
        print("=== KELOLA MODEL & STATISTIK ===")
        print("1. Tambah Model Baru")
        print("2. Hapus Model")
        print("3. Update Statistik Senjata")
        print("4. Kembali")
        pilih = input("Pilih opsi: ")

        if pilih == '1':
            tambah_model()
        elif pilih == '2':
            hapus_model()
        elif pilih == '3':
            update_statistik()
        elif pilih == '4':
            break
        else:
            print("Pilihan tidak valid!")
            pause()

def utama():
    while True:
        pilih = menu_login()
        if pilih == '1':
            status = ulang_login()
            while True:
                menu = menu_utama(status)
                if menu == '1':
                    tampil_rekomendasi()
                elif status == "admin" and menu == '2':
                    update_rekomendasi()
                elif status == "admin" and menu == '3':
                    kelola_model_statistik()
                elif (status == "admin" and menu == '4') or (status == "user" and menu == '2'):
                    print("Terima kasih, sampai jumpa!")
                    sys.exit()
                else:
                    print("Pilihan tidak valid!")
                    pause()
        elif pilih == '2':
            register()
        elif pilih == '3':
            print("Keluar dari program...")
            sys.exit()
        else:
            print("Pilihan tidak valid!")
            pause()

utama()
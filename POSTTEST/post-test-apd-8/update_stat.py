from fungsi import clear, pause
from data import jenis_senjata, model_senjata, semua_statistik

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
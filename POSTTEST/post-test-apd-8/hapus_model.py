from fungsi import clear
from data import jenis_senjata, model_senjata, semua_statistik

def hapus_model():
    clear()
    print("=== HAPUS MODEL & STATISTIK ===")
    for i in range(len(jenis_senjata)):
        print(str(i+1)+". "+jenis_senjata[i])
    print(str(len(jenis_senjata)+1)+". Kembali")
    try:
        jenis = int(input("Pilih jenis: ")) - 1
        if jenis == len(jenis_senjata):
            return
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
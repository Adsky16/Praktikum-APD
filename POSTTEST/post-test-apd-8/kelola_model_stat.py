from fungsi import clear, pause
from tambah_model import tambah_model
from hapus_model import hapus_model
from update_stat import update_statistik

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
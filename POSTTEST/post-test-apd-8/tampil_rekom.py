from fungsi import clear, pause
from data import jenis_senjata
from tampil_model_rekom import tampil_model_rekomendasi

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
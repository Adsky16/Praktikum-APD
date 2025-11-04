from fungsi import clear, pause
from data import jenis_senjata, rekomendasi_list
from tampil_stat import tampil_statistik


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
from fungsi import clear, pause
from data import data_user

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
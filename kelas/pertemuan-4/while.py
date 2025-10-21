while True:
    print("Menu")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")
    opsi = int(input("Pilih opsi (1-3): "))
    if opsi == 1:
        print("\nAnda memilih Option 1")
    elif opsi == 2:
        print("Anda memilih Option 2")
    elif opsi == 3:
        print("Keluar dari program.")
        break
    else:
        print("\nOpsi tidak valid, silakan coba lagi.")
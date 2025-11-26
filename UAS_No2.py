from collections import deque

stack = deque()

def tampilkan_menu():
    print("\nMenu Stack:")
    print("1). Append (Tambah ke kanan)")
    print("2). AppendLeft (Tambah ke kiri)")
    print("3). Pop (hapus elemen kanan)")
    print("4). PopLeft (hapus elemen kiri)")
    print("5). Clear (Kosongkan stack)")
    print("6). Keluar")
    print(f"Stack saat ini: {list(stack)}")

def main():
    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1-6): "))
        except ValueError:
            print("Input tidak valid. Masukkan angka 1-6.")
            continue
        
        if pilihan == 1:
            nilai = input("Masukkan nilai untuk append: ")
            stack.append(nilai)
            print(f"Nilai '{nilai}' ditambahkan ke kanan.")
        
        elif pilihan == 2:
            nilai = input("Masukkan nilai untuk append left: ")
            stack.appendleft(nilai)
            print(f"Nilai '{nilai}' ditambahkan ke kiri.")
        
        elif pilihan == 3:
            if stack:
                nilai = stack.pop()
                print(f"Nilai '{nilai}' hapus elemen kanan.")
            else:
                print("Stack kosong, tidak bisa pop.")
        
        elif pilihan == 4:
            if stack:
                nilai = stack.popleft()
                print(f"Nilai '{nilai}' hapus elemen kiri.")
            else:
                print("Stack kosong, tidak bisa pop left.")
        
        elif pilihan == 5:
            stack.clear()
            print("Stack dikosongkan.")
        
        elif pilihan == 6:
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih 1-6.")

if __name__ == "__main__":
    main()

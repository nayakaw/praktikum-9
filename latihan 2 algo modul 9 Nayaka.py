def buatFile():
    file = open("modul9_3.txt", 'w')
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    angkatan = input("Masukkan Angkatan: ")
    file.write("Nama: " + nama)
    file.write("\nNIM: " + nim)
    file.write("\nAngkatan: " + angkatan)
    file.close()

def bacaFile():
    file = open("modul9_3.txt", "r")
    text = file.read()
    print(text)
    file.close()
    
def updateFile():
    file = open("modul9_3.txt", 'a')
    sahabat = input("Masukkan nama sahabatmu: ")
    catatan = input("Masukkan catatan tambahanmu: ")
    file.write("\nSahabat: " + sahabat)
    file.write("\nCatatan: " + catatan)
    file.close()

def main():
    repeat = True
    while (repeat):
        print("=== Program File Handling - Nayaka ===")
        print("1. Membuat & Menulis File")
        print("2. Membaca File")
        print("3. Update File")
        print("4. keluar dari Program")
        pilih = int(input("Masukkan nomor pilihan Anda: "))
        
        if (pilih == 1):
            print("\n")
            buatFile()
            print("\n")
        elif (pilih == 2):
            print("\n")
            bacaFile()
            print("\n")
        elif (pilih == 3):
            print("\n")
            updateFile()
            print("\n")
        elif (pilih == 4):
            print("Terima kasih telah menggunakan program saya")
            repeat = False
        else:
            print("Masukkan nomor yang ada di list!")
            print("\n")
            
main()
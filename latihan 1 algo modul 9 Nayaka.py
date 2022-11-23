def buatfile(a,b,c,d,e):
    file = open('Biodata.txt','w')
    file.write(f'Nama : {a} \nUmur : {b} \nAlamat : {c} \nEmail : {d} \nDosen wali : {e}')
    file.close()
    
def bacafile():
    file = open('Biodata.txt','r')
    text = file.read()
    print(text)
    file.close()

a = input("Masukkan Nama mu: ")
b = input("Masukkan Umur mu: ")
c = input("Masukkan Alamatmu: ")
d = input("Masukkan Emailmu: ")
e = input("Masukkan Dosen Walimu: ")
print("\nBerikut Biodatamu")
buatfile(a,b,c,d,e)
bacafile()
# percabangan
# struktur
"""
    1. if -nya
    2. punya kondisi
    3. punya aksi
"""
nama = input("masukkan nama : ")

# percabangan yang inline (satu baris)
if nama == "azian" : print("Selamat Datang")
print("Terima Kasih")

# percabangan identasi
if nama == "azian" :
    print("Selamat Datang")
    print("selamat Belajar python")
print("Bukan Bagian percabangan")

# percabangan 1 kondisi dan 2 aksi
# pakai kata kunci "else"

if nama == "azian" :
    print("Selamat Datang {nama}")
else :
    print(f' anda {nama}, bukan azian')
print("Terima kasih")    
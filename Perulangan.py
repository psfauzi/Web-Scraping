"""
Program perulangan membaca buku

"""

jumlah_buku = 100
print("Ibu berkata,Baca Semua buku")

jumlah_buku_yang_bisa_dibaca = 0

for jumlah_buku_yang_bisa_dibaca in range(1, jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_bisa_dibaca} sudah dibaca")

print(f"Jumlah buku yang sudah dibaca {jumlah_buku_yang_bisa_dibaca}")

# tanpa for
print("Membaca for")
print("Membaca buku ke-1")
print("Membaca buku ke-2")
print("Membaca buku ke-3")
print("Membaca buku ke-4")
print("Membaca buku ke-5")
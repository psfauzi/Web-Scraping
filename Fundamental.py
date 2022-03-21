"""
Semua sintaks dasar bahasa pemrograman terdiri dari:
1. Sekuensial: Langkah berurutan
2. Percabangan : Langkah melompat jika kondisi terpenuhi
3. Perulangan: mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi

"""
print("Ibu berkata pergi ke toko")

#percabangan

jumlah_botol_susu = 173
jumlah_telur = 1587
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah telur {jumlah_telur} butir")


if jumlah_botol_susu >0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")
else:
    print("Budi tidak jadi membeli 1 botol susu")

print("Budi pulang kerumah")
print("Menyampaikan hasilnya kepada ibu")


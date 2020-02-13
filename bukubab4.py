# # studi kasus 1
# # jumlah segitiga
# jumlah_segitiga = 123
# # alas dan tinggi segitiga
# alas = 30
# tinggi = 18
# #luas segitiga
# luas = alas*tinggi/2
# print("luas segitiga = ", luas)
# # luas total segitiga
# luas_total_segitiga = luas * jumlah_segitiga
# print("luas 123 buah segitiga adalah ", luas_total_segitiga, " satuan luas")

# # studi kasus 2
# # informasi kamar
# total_kamar = int(input("Total kamar pak Amir = "))
# panjang_kamar = int(input("Panjang kamar pak Amir = "))*100
# lebar_kamar = int(input("Lebar kamar pak Amir = "))*100
# luas_kamar = panjang_kamar*lebar_kamar
# print("luas satu kamar pak Amir adalah ", luas_kamar, " sentimeter persegi")
# total_luas_kamar = luas_kamar*total_kamar
# print("Luas", total_kamar, "kamar pak Amir adalah ", total_luas_kamar)
# # informasi ubin
# lebar_ubin = int(input("masukan lebar ubin = "))
# panjang_ubin = int(input("masukan panjang ubin = "))
# luas_ubin = (lebar_ubin*panjang_ubin)
# print("Luas ubin = ", luas_ubin, "sentimeter persegi")
# # ubin yang dibutuhkan
# ubin_yang_dibutuhkan = total_luas_kamar/luas_ubin
# print("pak amir membutuhkan ", ubin_yang_dibutuhkan , "buah, untuk mengubin ", total_kamar, "kamar, milik pak Amir")

# #kasus3
# jarakAdanB = 128783082 
# dalamKM = jarakAdanB // 100000
# dalamM = (jarakAdanB % 100000) // 100
# dalamcm = (jarakAdanB % 100000) % 100
# print("jarak kota A dan B adalah ", dalamKM ," KM, ", dalamM, " M, ", dalamcm, " CM " )

# # soal 1
# # informasi kamar
# total_kamar = int(input("Total kamar pak Amir = "))
# panjang_kamar = int(input("Panjang kamar pak Amir = "))*100
# lebar_kamar = int(input("Lebar kamar pak Amir = "))*100
# luas_kamar = panjang_kamar*lebar_kamar
# print("luas satu kamar pak Amir adalah ", luas_kamar, " sentimeter persegi")
# total_luas_kamar = luas_kamar*total_kamar
# print("Luas", total_kamar, "kamar pak Amir adalah ", total_luas_kamar)
# # informasi ubin
# lebar_ubin = int(input("masukan lebar ubin = "))
# panjang_ubin = int(input("masukan panjang ubin = "))
# luas_ubin = (lebar_ubin*panjang_ubin)
# print("Luas ubin = ", luas_ubin, "sentimeter persegi")
# # ubin yang dibutuhkan
# ubin_yang_dibutuhkan = total_luas_kamar//luas_ubin
# print("pak amir membutuhkan ", ubin_yang_dibutuhkan , "buah, untuk mengubin ", total_kamar, "kamar, milik pak Amir")
# # total box
# isiubindalambox = 5
# total_box = round(ubin_yang_dibutuhkan / isiubindalambox)
# print("pak amir harus membeli " , total_box , "box ubin")

# soal 2
# informasi kamar
# total_kamar = int(input("Total kamar pak Amir = "))
# panjang_kamar = int(input("Panjang kamar pak Amir = "))*100
# lebar_kamar = int(input("Lebar kamar pak Amir = "))*100
# luas_kamar = panjang_kamar*lebar_kamar
# print("luas satu kamar pak Amir adalah ", luas_kamar, " sentimeter persegi")
# total_luas_kamar = luas_kamar*total_kamar
# print("Luas", total_kamar, "kamar pak Amir adalah ", total_luas_kamar)
# # informasi ubin
# lebar_ubin = int(input("masukan lebar ubin = "))
# panjang_ubin = int(input("masukan panjang ubin = "))
# luas_ubin = (lebar_ubin*panjang_ubin)
# print("Luas ubin = ", luas_ubin, "sentimeter persegi")
# # ubin yang dibutuhkan
# ubin_yang_dibutuhkan = total_luas_kamar/luas_ubin
# print("pak amir membutuhkan ", ubin_yang_dibutuhkan , "buah, untuk mengubin ", total_kamar, "kamar, milik pak Amir")
# # cadangan 10%
# totalubindancadangan = ubin_yang_dibutuhkan *1.1
# print("total ubin berserta cadangannya ", totalubindancadangan, " buah")
# # total box
# isiubindalambox = 5
# total_box = round(totalubindancadangan / isiubindalambox)
# print("pak amir harus membeli " , total_box , "box ubin")

# #soal 3
# informasi kamar
# total_kamar = int(input("Total kamar pak Amir = "))
# panjang_kamar = int(input("Panjang kamar pak Amir = "))*100
# lebar_kamar = int(input("Lebar kamar pak Amir = "))*100
# luas_kamar = panjang_kamar*lebar_kamar
# print("luas satu kamar pak Amir adalah ", luas_kamar, " sentimeter persegi")
# total_luas_kamar = luas_kamar*total_kamar
# print("Luas", total_kamar, "kamar pak Amir adalah ", total_luas_kamar)
# # informasi ubin
# lebar_ubin = int(input("masukan lebar ubin = "))
# panjang_ubin = int(input("masukan panjang ubin = "))
# luas_ubin = (lebar_ubin*panjang_ubin)
# print("Luas ubin = ", luas_ubin, "sentimeter persegi")
# # ubin yang dibutuhkan
# ubin_yang_dibutuhkan = total_luas_kamar/luas_ubin
# print("pak amir membutuhkan ", ubin_yang_dibutuhkan , "buah, untuk mengubin ", total_kamar, "kamar, milik pak Amir")
# # cadangan 10%
# totalubindancadangan = ubin_yang_dibutuhkan *1.1
# print("total ubin berserta cadangannya ", totalubindancadangan, " buah")
# # total box
# isiubindalambox = 5
# total_box = round(totalubindancadangan / isiubindalambox)
# print("pak amir harus membeli " , total_box , "box ubin")
# # harga total membeli ubin
# harga_1_box = 125000
# harga_total = total_box * harga_1_box
# print("Harga total = ", harga_total) 

# soal 4
# Uang maman
# uang_maman = 32892700
# dalam_100_ribu = uang_maman // 100000
# dalam_50_ribu = (uang_maman % 100000) // 50000
# dalam_20_ribu = ((uang_maman % 100000) % 50000 ) //20000
# dalam_10_ribu = (((uang_maman % 100000) % 50000) %20000) //10000
# dalam_5_ribu = ((((uang_maman % 100000) % 50000) %20000) % 10000) //5000
# dalam_1_ribu = (((((uang_maman % 100000) % 50000) %20000) % 10000) % 5000)//1000
# dalam_500 = ((((((uang_maman % 100000) % 50000) %20000) % 10000) % 5000)%1000)//500
# dalam_100 = (((((((uang_maman % 100000) % 50000) %20000) % 10000) % 5000)%1000)%500)//100
# print("uang pak maman sebesar ", uang_maman, " mendapat 100ribu sebanyak ", dalam_100_ribu ," lembar, ", " 50ribu ", dalam_50_ribu, " lembar, ", " 20ribu ",  dalam_20_ribu, " lembar, ", "dalam 10 ribu", dalam_10_ribu , " lembar, ", "dalam 5000 ", dalam_5_ribu, " lembar, ", " dalam 1000 ", dalam_1_ribu, " lembar, ", "dalam 500 ", dalam_500, " koin, ", "dalam 100 ", dalam_100 ," koin" )

# # soal 5
# # lingkaran
# import math
# print(math.pi)
# jarijari = float(input("masukan jari jari lingkaran = "))
# luas_lingkaran = round( math.pi * (jarijari**2),4)
# print("luas lingkaran = ", luas_lingkaran ,"satuan")

# soal 6


# # soal 7 
# strawberry = 30000
# jeruk = 15000
# anggur = 42000
# apel = 38000
# semangka = 21000
# beli_str = int(input("masukan berapa kg strawberry yang mau dibeli = "))
# harga_total_strawberry = beli_str*strawberry
# beli_jeruk = int(input("masukan berapa kg jeruk yang mau di beli = "))
# harga_total_jeruk = beli_jeruk*jeruk
# beli_anggur = int(input("masukan berapa kg anggur yang mau di beli = "))
# harga_total_anggur = beli_anggur*anggur
# beli_apel = int(input("masukan berapa kg apel yang mau di beli = "))
# harga_total_apel = beli_apel*apel
# beli_semangka = int(input("masukan berapa kg semangka yang mau di beli = "))
# harga_total_Semangka = beli_semangka*semangka
# total = harga_total_anggur+harga_total_apel+harga_total_jeruk+harga_total_Semangka+harga_total_strawberry
# print("total yang harus dibayarkan = ", total)

# soal 8
# COGS
# modal_str = 25000
# modal_jeruk = 12500
# modal_anggur = 39000
# modal_apel = 35500
# modal_semangka = 19200
# # harga jual
# strawberry = 30000
# jeruk = 15000
# anggur = 42000
# apel = 38000
# semangka = 21000
# # total sales
# beli_str = int(input("masukan berapa kg strawberry yang mau dibeli = "))
# harga_total_strawberry = beli_str*strawberry
# beli_jeruk = int(input("masukan berapa kg jeruk yang mau di beli = "))
# harga_total_jeruk = beli_jeruk*jeruk
# beli_anggur = int(input("masukan berapa kg anggur yang mau di beli = "))
# harga_total_anggur = beli_anggur*anggur
# beli_apel = int(input("masukan berapa kg apel yang mau di beli = "))
# harga_total_apel = beli_apel*apel
# beli_semangka = int(input("masukan berapa kg semangka yang mau di beli = "))
# harga_total_Semangka = beli_semangka*semangka
# # gross profit
# profit_str = harga_total_strawberry - (modal_str*beli_str)
# profit_jeruk = harga_total_jeruk - (modal_jeruk*beli_jeruk)
# profit_anggur = harga_total_anggur - (modal_anggur*beli_anggur)
# profit_apel = harga_total_apel - (modal_apel*beli_apel)
# profit_semangka = harga_total_Semangka - (modal_semangka*beli_semangka)
# total_profit = profit_anggur + profit_apel + profit_jeruk + profit_semangka + profit_str 
# print("total profit menjual buah adalah ", total_profit, "Rupiah")

# soal 9
# total_belanjaan = int(input("total belanjaan = "))
# x = total_belanjaan-(total_belanjaan%1000)
# print("total yang harus di bayar = ",x, " Rupiah")

# soal 10
import math
No_komputer = input("Masukan nomor komputer = ")
print("waktu mulai akses = ")
Jam_mulai = int(input("Jam mulai akses = "))*3600
Menit_mulai = int(input("Menit mulai akses = "))*60
detik_mulai = int(input("detik mulai akses = "))
total_mulai = Jam_mulai+Menit_mulai+detik_mulai 
print("waktu selesai akses = ")
Jam_selesai = int(input("Jam selesai akses = "))*3600
Menit_selesai = int(input("Menit selesai akses = "))*60
detik_selesai = int(input("detik selesai akses = "))
total_selesai = Jam_selesai+Menit_selesai+detik_selesai
total_rent = math.ceil((total_selesai-total_mulai ) /1800)
biaya_Rent = total_rent * 2250
print(biaya_Rent)
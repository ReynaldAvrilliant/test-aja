# Angka1 = int(input("masukan angka 1 = "))
# Angka2 = int(input("masukan angka 2 = "))
# print(Angka1*Angka2)
# print(Angka1/Angka2)
# print(Angka1+Angka2)
# print(Angka1-Angka2)
# print(Angka1%Angka2)
# print(Angka1**2)

# angka_1 = int(input("masukan angka berapapun = "))
# angka_2 = int(input("masukan angka lain = "))
# angka_1 +=3
# angka_2 *=4
# print(angka_1)
# print(angka_2)

# import math

# print(math.pi);
# print(math.pow(8, 2))
# print(math.fabs(-5.2))
# print(math.sqrt(64))

# print(round(4.7))
# print(round(4.3))
# print(math.floor(4.7))
# print(math.ceil(4.4))

x = "hello world";
# print(len(x));
# print(x.index("world"));
print(x.split("  "));
# print(x.lower());
# print(x.upper());
# print(x.capitalize());

# text = "I'm Reynald, nice to meet you";
# print(text[1])
# print(text[2:])
# print(text[:4])
# print(text[2:5])
# print(text[:])

# x = 4
# y = 3
# z = 2
# w = ((x+y*z)/(x*y))**z
# print(w)

# import math
# Angka = int(input("Silahkan masukan angka berapapun = "))
# print(Angka**2)
# print(math.pow(Angka, 2))
# import math
# total_hari = 485
# total_tahun = int(total_hari/360)
# sisa_tahun = int(total_hari%360)
# total_bulan = int(sisa_tahun/30)
# sisa_bulan = int(sisa_tahun%30)
# total_minggu = int(sisa_bulan/7)
# sisa_minggu = int(sisa_bulan%7)
# total_hari = int(sisa_minggu)
# print(int(total_tahun))
# print(int(sisa_tahun))
# print(int(total_bulan))
# print(int(sisa_bulan))
# print(int(total_minggu))
# print(int(sisa_minggu))
# print(int(total_hari))

# print(total_tahun , " Tahun " , total_bulan , " Bulan " , total_minggu , " Minggu " , total_hari , " Hari ");

# andi + budi = 49
# andi / budi = 0.4
# # total_ratio = 0.4 + 1
# andi = int(49 * (0.4/1.4))
# budi = int(49 * (1/1.4))
# andi_2_tahun_lagi = int(andi+2)
# budi_2_tahun_lagi = int(budi+2)
# print("Umur Andi dan Budi 2 Tahun lagi adalah" , andi_2_tahun_lagi , " dan " , budi_2_tahun_lagi)

# text = "halo dunia"
# print(text.count("a"))

# Jarak mobil A dan B = 120
# Kecepatan mobil A = 60
# Kecepatan mobil B = 40
# import math
# Mobil_A = 60
# Mobil_B = 40
# Jarak = 120
# Satuan = 60
# Waktu_Tabkrakan = int(Jarak/(Mobil_A+Mobil_B))
# sisa_menit = (Jarak/(Mobil_A+Mobil_B))%1
# total_menit = float(sisa_menit*60)
# waktu_sekarang = 9
# waktu_tabrakan_jalan = waktu_sekarang + Waktu_Tabkrakan
# print("Waktu kedua mobil itu tabrakan adalah jam ", waktu_tabrakan_jalan ,":" , round(total_menit))

# x = "ini string"
# print(len(x))
# print(x.lower())
# print(x.upper())

# print(x.lower().islower())
# print(type(x.upper().islower))
# print(x.upper().isupper())
# print(x.lower().isupper())

# y = "purwadhika"
# print(len(y))
# print(y[0])
# print(y[9])
# print(y.count("a"))
# print(y[0:5])
# print(y[0:len(y)])
# print(y[0:10:2])
# print(y[0:10:3])
# print(y.index("p"))
# print(y.index("wa"))

# angka = int(input("masukan angka = "))
# if (angka%2 == 0):
#     print("angka " , angka , " genap");
# else:
#     print("angka" , angka ,  " ganjil")

# z = "Andi ditara"
# # print(z.replace("A" , "O"))
# # print(z.replace("a" , "i"))
# # print(z.replace("di" , "na"))
# # z.replace("a","o")
# # z.replace("i" , "o")
# z= z.replace("a","o").replace("i","o")
# print(z)

# nama = "budi"
# usia = 22
# print("halo saya {} usia {}".format(nama,usia))
# print(f"halo saya {nama} usia {usia}")
# print("halo saya", nama , "usia ", usia)
# print("halo saya %s usia %d" %(nama,usia))

# kata = "Purwadhika Startup and Coding school"
# print(len(kata.replace(" ","")))
# print(kata.count("a"))
# # print(len(kata)) - len(kata.replace("a",""))
# print(kata.upper().count("P"))

# kata = "hari ini hari tidak masuk sekolah karena hari libur"
# cari = "hari"
# print(kata.count("hari"))
# print(kata.upper().count("HARI"))
# selisih = len(kata) - len(kata.lower().replace(cari,""))
# jmlcari = selisih / len(cari)

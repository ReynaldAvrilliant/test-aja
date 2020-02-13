# # studi kasus 1
# nilaianda = int(input("masukan nilai anda = "))
# if (nilaianda>=80 and nilaianda<=100):
#     print("Nilai kamu memiliki grade A")
# elif (nilaianda>=70 and nilaianda<=79):
#     print("nilai kamu memiliki grade B")
# elif(nilaianda>=60 and nilaianda<=69):
#     print("nilai kamu memiliki grade C")
# elif (nilaianda>=59 and nilaianda<=40):
#     print("nilai kamu memiliki grade D")
# elif (nilaianda>=0 and nilaianda<=39 ):
#     print("nilai kamu memiliki grade E")
# else:
#     print("anda salah memasukan nilai")

#   # studi kasus 2
# # jawab = "y"
# while jawab == "y":
#     bil1 = int(input("masukan bilangan 1 = "))
#     bil2 = int(input("masukan bilangan 2 = "))
#     hasil = bil1+bil2
#     print("hasil perjumlahan ke 2 bilangan tsb adalah = ", hasil)
#     jawab = input("ingin mengulanginya lagi (y/n)? ")
#     if jawab == "n":
#         break


# #studi kasus 3
# anak_ayam = int(input("masukan jumlah anak ayam sekarang "))
# while anak_ayam>=1:
#     if anak_ayam>1:
#          print("anak ayam turun ", anak_ayam, "mati satu tinggal ", anak_ayam-1)
#     else:
#         print("anak ayam turun ", anak_ayam, "mati satu tinggal induknya")
#     anak_ayam-=1

# studi kasus 4

# for num in range (1,100):
#     bil = num + 1
#     if bil % 3 == 0:
#         print(bil)

# for i in range (1,100):
#     if (i) % 3 == 0:
#         print(i)

# for i in range(1,100):
#     if i %3 == 0:
#         print(i)

# n = int()
# x = int(input("masukan total bilangan = "))
# for n in range (x):
#     if n%3 ==0:
#         print(n+1)

# studi kasus 5
# sum = 0 
# for i in range (100):
#     if(i+1)%3 == 0:
#         sum = sum + 1
# print("banyaknya bilangan " + str(sum))

# # studi kasus 6
# sum = 0
# x = int(input("masukan bilangan = "))
# for i in range (x):
#     suku = i + 1
#     sum = sum +suku
# print("hasil perjumlahan = "+ str(sum))

# x = int(input("masukan angka awal = "))
# y = int(input("masukan angka akhir = "))
# sum = 0
# for i in range (x+1,y+1):
#     x = x+i
# print("hasil perjumlahan = "+str(x))

# studi kasus 7
# hitung = 0
# sum = 0
# x = int(input("masukan angka awal = "))
# y = int(input("masukan angka akhir = "))
# for i in range (x,y):
#     if i % 3 == 0 and i % 5 == 0:
#         hitung = hitung + 1
#         sum = sum + i
#         print(i)
# print("banyak bilangan = ", str(hitung))
# print("jumlahan bilangan = ", str(sum))
        
    
# proyek latihan
# soal 1
# nilai_bahasa_indonesia = int(input("Masukan nilai bahasa indonesia = "))
# nilai_mat = int(input("masukan nilai matematika = "))
# nilai_ipa = int(input("Masukan nilai IPA = "))
# if (nilai_mat<70 or nilai_bahasa_indonesia < 60 or nilai_ipa < 60):
#     print("status kelulusan = TIDAK LULUS")
# else :
#     print("status kelulusan = LULUS")

# # Soal 2
# nilai_Bindo = int(input("masukan nilai bahasa indonesia = "))
# nilai_matematika = int(input("masukan nilai matematika = "))
# nilai_ipa = int(input("masukan nilai ipa = "))
# if (nilai_matematika<70 or nilai_Bindo < 60 or nilai_ipa < 60):
#     print("Tidak Lulus")
#     if(nilai_matematika<70):
#         print("Tidak lulus karena nilai matematika di bawah 70")
#     if(nilai_Bindo<60):
#         print("tidak lulus kerena nilai Bahasa indonesia di bawah 60")
#     if (nilai_ipa<60):
#         print("tidak lulus karena nilai Ipa di bawah 60")
# else : 
#     print("lulus")

# # soal 3
# A = 10000000
# B = 8500000
# C = 7000000
# D = 5000000
# tax_A = 0.025
# tax_B = 0.02
# tax_C = 0.015
# tax_D = 0.01
# potongan_A = A*tax_A
# potongan_B = B*tax_B
# potongan_C = C*tax_C
# potongan_D = D*tax_D
# kode_karyawan = input("masukan kode karyawan = ")
# masukan_nama_karyawan = input("masukan nama karyawan = ")
# masukan_gol_karyawan = input("masukan golongan karyawan = ").upper()
# print(" = = = = = = = = = = = = = = = = = = = = ")
# print("STRUK RINCIAN GAJI KARYAWAN")
# print(" = = = = = = = = = = = = = = = = = = = = ")
# print("Nama karyawan = "+ masukan_nama_karyawan)
# print("Golongan = "+ masukan_gol_karyawan)
# print(" = = = = = = = = = = = = = = = = = = = = ")
# if (masukan_gol_karyawan == "A"):
#     print("Gaji pokok = Rp ", A)
# elif(masukan_gol_karyawan == "B"):
#     print("Gaji pokok = Rp ", B)
# elif(masukan_gol_karyawan == "C"):
#     print("Gaji pokok = Rp ", D)
# else:
#     print("Gaji pokok = Rp. 5.000.000")
# if(masukan_gol_karyawan =="A"):
#     print("Potongan (2.5%) = ", potongan_A)
# elif(masukan_gol_karyawan =="B"):
#     print("potongan (2%) = ", potongan_B)
# elif(masukan_gol_karyawan == "C"):
#     print("potongan (1.5%) = ", potongan_C)
# else:
#     print("potongan(1%) = ", potongan_D)
# print(" = = = = = = = = = = = = = = = = = = = = ")
# if(masukan_gol_karyawan =="A"):
#     print("Total Gaji = ", A-potongan_A)
# elif(masukan_gol_karyawan =="B"):
#     print("Total Gaji = ", B-potongan_B)
# elif(masukan_gol_karyawan =="C"):
#     print("Total Gaji = ", C-potongan_C)
# else:
#     print("Total Gaji = ", D-potongan_D)

# soal nomor 4
# A = 10000000
# B = 8500000
# C = 7000000
# D = 5000000
# tax_A = 0.025
# tax_B = 0.02
# tax_C = 0.015
# tax_D = 0.01
# tunjangan_m = 0.1
# tunjangan_a = 0.05
# potongan_A = A*tax_A
# potongan_B = B*tax_B
# potongan_C = C*tax_C
# potongan_D = D*tax_D
# kode_karyawan = input("masukan kode karyawan = ")
# masukan_nama_karyawan = input("masukan nama karyawan = ")
# masukan_gol_karyawan = input("masukan golongan karyawan = ").upper()
# status = input("Apakah anda sudah menikah ? (Y/N) = ").upper()
# anak = int(input("masukan jumlah anak = "))
# print(" = = = = = = = = = = = = = = = = = = = = ")
# print("STRUK RINCIAN GAJI KARYAWAN")
# print(" = = = = = = = = = = = = = = = = = = = = ")
# print("Nama karyawan = "+ masukan_nama_karyawan)
# print("Golongan = "+ masukan_gol_karyawan)
# print(" = = = = = = = = = = = = = = = = = = = = ")
# if (masukan_gol_karyawan == "A"):
#     Gaji_pokok = A
#     print("Gaji pokok = Rp ", A)
# elif(masukan_gol_karyawan == "B"):
#     Gaji_pokok = B
#     print("Gaji pokok = Rp ", B)
# elif(masukan_gol_karyawan == "C"):
#     Gaji_pokok = C
#     print("Gaji pokok = Rp ", C)
# elif(masukan_gol_karyawan == "D"):
#     Gaji_pokok = D
#     print("Gaji pokok = Rp ", D)
# if(masukan_gol_karyawan =="A"):
#     print("Potongan (2.5%) = ", potongan_A)
# elif(masukan_gol_karyawan =="B"):
#     print("potongan (2%) = ", potongan_B)
# elif(masukan_gol_karyawan == "C"):
#     print("potongan (1.5%) = ", potongan_C)
# else:
#     print("potongan(1%) = ", potongan_D)
# print(" = = = = = = = = = = = = = = = = = = = = ")
# print("Tunjangan Menikah")
# print(" = = = = = = = = = = = = = = = = = = = = ")
# if status == "Y":
#     tunjangan_menikah = Gaji_pokok*tunjangan_m
#     print("tunjangan istri / suami sebesar = Rp. ", tunjangan_menikah)
# else:
#     tunjangan_menikah = Gaji_pokok*0
#     print("tunjangan istri / suami sebesar = Rp. ", tunjangan_menikah)
# print(" = = = = = = = = = = = = = = = = = = = = ")
# print("Tunjangan Anak")
# print(" = = = = = = = = = = = = = = = = = = = = ")
# if anak > 0:
#     tunjangan_anak = (Gaji_pokok*tunjangan_a)*anak
#     print("tunjangan anak sebesar = Rp. ", tunjangan_anak)
# else :
#     tunjangan_anak = (Gaji_pokok*0)*anak
#     print("Tunjangan anak sebesar = Rp. ", tunjangan_anak)
# print(" = = = = = = = = = = = = = = = = = = = = ")
# if(masukan_gol_karyawan =="A"):
#     print("Total Gaji = ", (A-potongan_A)+tunjangan_anak+tunjangan_menikah)
# elif(masukan_gol_karyawan =="B"):
#     print("Total Gaji = ", (B-potongan_B)+tunjangan_anak+tunjangan_menikah)
# elif(masukan_gol_karyawan =="C"):
#     print("Total Gaji = ", (C-potongan_C)+tunjangan_anak+tunjangan_menikah)
# else:
#     print("Total Gaji = ", (D-potongan_D)+tunjangan_anak+tunjangan_menikah)

# soal nomor 5
# x = int(input("masukan range yang di inginkan = "))

# hitung = 0
# sum = 0
# for i in range (x):

#     if(i%2 != 0):
#         hitung = hitung +1
#         sum = sum+i
# print("banyaknya bil ganjil = ", str(hitung))
# print("total penjumlahan bil ganjil = ", str(sum))

# soal nomor 6
# bintang =""
# for i in range (5):
#     for j in range (0,i+1):
#         bintang += " * "
#     bintang += "\n"
# print(bintang)
bintang =""
for i in range (5,0,-1):
    for j in range (i):
        bintang += " * "
    bintang += "\n"
print(bintang)

# # soal no 7
# angka = 72
# inputuser = ""
# trial = 1
# limit = 10
# over = False
# while angka != inputuser and not over:
#     if trial<=limit:
#         inputuser = int(input("masukan tebakan angka yang saya pilih dari 1 hingga 100 = "))
#         if inputuser != angka and trial<=limit :
#             trial+=1
#             if(inputuser>angka):
#                 print("tebakan anda ke", trial, "salah, coba lagi! ", inputuser, " kebesaran")
#             elif(inputuser<angka):
#                 print("tebakan anda ke", trial, "salah, coba lagi! ", inputuser, " kekecilan")
#         elif inputuser != angka and trial>limit :
#             trial+=1
#             print("tebakan anda ke", trial, "kesempatan anda habis")
#         else:
#             print("tebakan anda benar ")
#     else:
#         over = True
#         print("coba lain waktu")




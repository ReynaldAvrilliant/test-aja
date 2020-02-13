# soal 1
# ayam + kambing = 13
# kaki ayam + kaki kambing = 32
# ayam = 2
# kambing = 4
# a+k = 13
# k = 13 - a
# 2a + 4k = 32
# 2a + 4(13-a) = 32
# 2a + 52 - 4a = 32
# -2a = 32 - 52
#  a = -20 /- 2
#  a = 10
# jawaban
import math
Jumlah_ayam_dan_kambing = int(input("Masukan jumlah ayam dan kambing = "))
jumlah_kaki_ayam_dan_kambing = int(input("masukan jumlah kaki ayam dan kambing = "))
ayam = float(4*Jumlah_ayam_dan_kambing - jumlah_kaki_ayam_dan_kambing)/2
kambing = float(Jumlah_ayam_dan_kambing-ayam)
print("Jumlah ayam yang ada adalah = " , ayam , " ekor")
print("Jumlah kambing yang ada adalah = ", kambing,  "ekor")

# soal2
# ayah_tambah_andi = 56
# total_ratio = 7
# jawaban
import math
total_umur_ayah_dan_andi = float(input("Total umur ayah dan andi = "))
rasio_umur_ayah_dan_andi = float(input("rasio umur ayah = "))
umur_ayah = round(total_umur_ayah_dan_andi/(rasio_umur_ayah_dan_andi+1))
umur_andi = round(total_umur_ayah_dan_andi-umur_ayah)
print("umur ayah adalah ", umur_ayah , " tahun")
print("umur andi adalah " , umur_andi, " tahun" )


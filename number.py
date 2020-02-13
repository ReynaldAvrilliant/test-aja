# x = 12
# y = 34.8

# print((1+3)/(4-2))
# print((1+3)//(4-2))
# print(int(12/5))
# print(float(12/5))
# print(2**12)
# print(5**5)
# print(10%4)
# print(abs(-10000))
print(round(3.24566456,3))
# print(round(3.766978,3))
# print(max(1,2,3,4,5,6,7,8,9))
# print(min(1,2,3,4,5,6,7,8,9))
# print()

# ayam + kambing = 13
# kaki ayam + kaki kambing = 32
# ayam = 2
# kambing = 4

# a + k = 13 = k = 13-a 
# 2a + 4k = 32
# 4(13-a) + 2a = 32
# 52 -4a + 2a = 32
# 52 - 2a = 32
# a = (52-32)/2

totalekor = 13
totalkaki = 32
ayam = (4 * totalekor - totalkaki) / 2
kambing = (totalekor - ayam)
print(f'jumlah kambing = {kambing} ekor')
print(f'jumlah ayam = {ayam} ekor')
# 
# ayah_tambah_andi = 56
# total_ratio = 7
# umur_ayah = 56*(5/7)
# umur_andi = 56*(2/7)
# print(umur_ayah)
# print(umur_andi)

# angka = int(input("ketik angka = "))
# print(angka**2)

# kalimat = input("ketik kalimat = ")
# cari = input("ketik huruf yang dicari = ")
# print(kalimat.count(cari))
# print("huruf" , cari , "ada" , kalimat.count(cari))

kalimat = input("ketik kalimat : ").lower()
cari = input("ketik huruf yang dicari : ").lower()
jmlcari = len(kalimat) - len(kalimat.replace(cari,""))
print(f"jumlah huruf {cari} = {jmlcari}")
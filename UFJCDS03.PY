# def kpk(a,b):
#     x = 1
#     y = 1
#     p = a * x
#     q = b * y
#     while p != q:
#         while p > q:
#             y = y+1
#             q = b*y
#         while p < q:
#             x = x + 1
#             p = a * x
#     if p == q:
#         print(p)

# def fpb(a,b):
#     while 1:
#         sisa = a%b
#         if sisa == 0:
#             break
#         a,b = b,sisa
#     print(b)


# kpk(6,8)
# fpb(70,80)

# nomor 1  fpb kpk
# bil1 = int(input("masukan bilangan 1 = "))
# bil2 = int(input("masukan bilangan 2 = "))
# # fpb
# for i in range (1,min(bil1,bil2)+1):
#     if bil1 % i == 0 and bil2 % i == 0: 
#         hasilfpb = i
# # kpk
# for i in range (1,(bil1*bil2)+1):
#     if i % bil1 == 0 and i % bil2 == 0:
#         hasilkpk = i
#         break

# print("hasil fpb dari ", bil1, " dan ", bil2," adalah ", hasilfpb)
# print("hasil kpk dari ", bil1, " dan ", bil2," adalah ", hasilkpk)

# nomor 2

# angka = int(input("masukan angka berapapun = "))
# hasil = []
# def param(angka):
#     if type(angka) == int:
#         hasil.append("Bulat")
#     if angka >= 0:
#         hasil.append("cacah")
#     if angka < 0:
#         hasil.append("negatif")
#     if angka > 0:
#         hasil.append("asli")
#     if angka%2 == 0:
#         hasil.append("genap")
#     if angka%2 != 0:
#         hasil.append("ganjil")
#     for i in range(2,angka):
#         if angka % i == 0:
#             hasil.append("komposit")
#     if "komposit" not in hasil:
#         hasil.append("prima")
#     return hasil
# print(param(angka))

# nomor 3

print("mau membaca berita apa hari sekara ?")
print("[1] Berita seputar teknologi")
print("[2] Berita seputar bisnis")
print("[3] Berita seputar olahraga")
print("[4] Berita seputar kesehatan")
print("[5] Berita seputar science ")
pilihan = input("ketik pilihan anda [ 1/2/3/4/5 ] = ")

import requests
if pilihan == "1":
    berita = "technology"
if pilihan == "2":
    berita = "business"
if pilihan == "3":
    berita = "sports"
if pilihan == "4":
    berita = "health"
if pilihan == "5":
    berita = "science"
url = f"https://newsapi.org/v2/top-headlines?country=id&category={berita}&apiKey=9840fac6423445aab088524fe425ba98"

data = requests.get(url)
berita = data.json()["articles"]
for i in range (5):
    print(i+1,berita[i]["title"])



# Function
# def halo():
#     print("halo")

# halo()

# def hai(nama):
#     print("hai",nama)
# hai("andi")
# hai("budi")

# def kali(angka1,angka2):
#     print(angka1*angka2)
# kali(1,2)
# kali(3,4)
# kali(5,6)

# def luaspersegi(sisi):
#     luas = sisi** 2
#     print(f"luas persegi sisi = {sisi} adalah {luas}")

# luaspersegi(2)
# luaspersegi(8)
# luaspersegi(10)

# koverter usd to idr

# print("pilih metode koversi : ")
# print("1. USD => IDR ")
# print("2. IDR => USD ")
# print("metode pilihan : ")
# input("metode pilihan : ")
# input("masukkan nominal : ")

# def konverter ():
#     option = int(input("ketik 1 jika USD => IDR \n ketik 2 jika IDR => USD = "))
#     if(option == 1):
#         nominal_yang_ingin_dikonversi = int(input("nominal yang ingin diubah ke Rupiah = "))
#         USDtoIDR = nominal_yang_ingin_dikonversi * 13753
#         print("koversi USD to IDR =  ", USDtoIDR , " Rupiah")
#     else:
#         nominal_yang_ingin_dikonversi_keUSD = int(input("nominal yang ingin di ubah ke USD = "))
#         IDRtoUSD = nominal_yang_ingin_dikonversi_keUSD / 13753
#         print("konversi IDR to USD = ", IDRtoUSD , " USD")

# konverter()

# datakurs = {
#     "1": 14000,
#     "2": 0.00007
# }
# def konversi():
#     print("pilih metode konversi = ")
#     print("1. USD to IDR")
#     print("2. IDR to USD")
#     metode = input("ketik pilihan anda (1/2) = ")
#     if metode == "1":
#         nominal_USD = float(input("masukan nominal USD = "))
#         kurs = datakurs[metode]
#         rupiah = nominal_USD * kurs
#         print(f"USD {nominal_USD} setara = Rp {rupiah}")
#     elif metode =="2":
#         nominal = float(input("ketik nominal Rp : "))
#         kurs = datakurs[metode]
#         usd = nominal*kurs
#         print(f"Rp {nominal} setara = USD {usd}")
#     else: 
#         print("mohon maaf system saya belum cukup pintar ")
#         konversi()

# konversi()

# x = 99
# def halo():
#     global x 
#     x = x+5
#     print(x)
# halo()
# print(x)

# x = 12
# print(x)

# def halo():
#     return 12
# print(halo()*halo())

# def luaslingkaran(rad) :
#     area = 3.14 *rad*rad
#     return area
# print(luaslingkaran(8))

# def arealingkarann(rad):
#     area = 3.14 * rad * rad
#     print(area)
#     return area

# print(arealingkarann(7) * arealingkarann(7))

# while looping
# while condition
# x = 0
# while x <= 10:
#     print(x)
#     x = x + 1

# x = list(range(0,10000))
# # i = 0
# # while i<len(x):
# #     print(x[i])
# #     i+=1
# i = 0
# while i < len (x):
#     x[i]= (x[i]*2)
#     i+=1
# print(x)

# password = "12345"
# password2 = input("masukan password = ")
# while password2 != password  :
#     print("password anda salah!")
#     password2 = input("masukan password anda lagi = ")
#     if password2 == password:
#         print("anda berhasil login")
    
# password = "12345"
# inputuser = ""
# i=1

# while inputuser != password and i<=5:
#     inputuser = input("ketik password : ")
#     if inputuser != password and i<5 : 
#         print("password salah ! ")
#     elif i==5:
#         print("password salah ! ")
#         print("anda di blokir")
#     else :
#         print("password benar")
#     i+=1

inputuser = ""
password = "12345"
trial = 1
limit = 5
over = False
while inputuser != password and not over:
    if trial <= limit:
        inputuser = input("ketik password = ")
        if inputuser != password and trial <=limit:
            trial +=1 
            print(f"password salah coba lagi ! silahkan percobaan ke {trial}")
        elif inputuser!=password and trial > limit:
            trial +=1
            print("password salah, kesempatan habis")
        else : 
            print("password benar")
    else:
        over = True
        print("coba 1 jam lagi")
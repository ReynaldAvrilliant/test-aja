# x = int(input("masukan bilangan berapapun "))
# if (x%2 == 0):
#     print("bilangan", x, "bilangan genap")
# else :
#     print("bilangan", x, "bilangan ganjil")

# namahari = {
#     "senin":"monday","selasa":"tuesday","rabu":"wednesday",
#     "kamis":"thursday","jumat":"friday","sabtu":"saturday",
#     "minggu":"sunday"
# }
# x = input("ketik / wrtite = ").lower()
# if x in list(namahari.keys()):
#     print(f"bahasa inggrisnya {x} = {namahari[x]}")
# else : 
#     yIndo = list(namahari.keys())[list(namahari.values()).index(x)]
#     print(f"bahasa indonya {x} = {yIndo}")

# angka_1 = float(input("ketik angka 1 = "))
# operator = input("masukan operator (+ - / *)= ")
# angka_2 = float(input("masukan angka_2 = "))
# if (operator == "+"):
#     hasil = (angka_1 + angka_2)
#     print(angka_1,operator,angka_2 ," = ", hasil)
# elif(operator == "-"):
#     hasil = (angka_1 - angka_2)
#     print(angka_1,operator,angka_2 ," = ", hasil)
# elif(operator == "/"):
#     hasil = round((angka_1/angka_2),2)
#     print(angka_1,operator,angka_2 ," = ", hasil)
# else:
#     hasil = (angka_1*angka_2)
#     print(angka_1,operator,angka_2 ," = ", hasil)

# bb = float(input("masukan berat badan anda = "))
# tb = float(input("masukan tinggi badan anda (meter) = "))
# imt = (bb/(tb**2))
# if (imt<18.5):
#     print("anda under weight")
# elif (imt>=18.5 and imt<= 24.9):
#     print("anda normal")
# elif (imt>=25 and imt<= 29.9):
#     print("anda over weight")
# elif (imt>= 30 and imt<=39.9):
#     print("anda obese")
# else:
#     print("anda extreme obese")

username = ["andi", "budi", "caca"]
password = ["123","456","789"]

user = input("Ketik username = ").lower()
pwd = input("ketik password = ")

if user in username:
    idx = username.index(user)
    if pwd == password[idx]:
        print("berhasil login")
    else:
        print("password salah")
else:
    print("anda belum terdaftar")

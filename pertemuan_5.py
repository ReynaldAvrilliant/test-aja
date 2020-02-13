# namahari = {
#     "senin":"monday","selasa":"tuesday","rabu":"wednesday",
#     "kamis":"thursday","jumat":"friday","sabtu":"saturday",
#     "minggu":"sunday"
# }

# x = input("ketik nama hari : ").lower()
# xEnglish = namahari[x]
# print(f"English {x} = {xEnglish}")
# y = input("write day name : ")
# yIndo = list(namahari.keys())[list(namahari.values()).index(y)]
# print(f"bahasa {y} = {yIndo} ")

# primitive var
# list[]
# tuple (), "tidak bisa di edit"
# set {} bisa di tambah di edit dll, tapi elemennya immutable,no index
# dictonary {key:val}


# x = {1,2,3,4}
# print(x)
# y = {5,6,7} #dict tdk bs masuk dalam set
# print(y)

# x = {
#     "nama" : "andi",
#     "usia" : 21,
#     3 : True,
#     "mobil": ["pajero","innova"],
#     "coord":{
#         "lat":112.9,
#         "lon":45.9,
#         "gps":[112.9,45.9]
#     }

# }
# print(x["mobil"][0]) #pajero
# print(x["coord"]["gps"][1]) #45.9

namahari = {
    "senin":"monday","selasa":"tuesday","rabu":"wednesday",
    "kamis":"thursday","jumat":"friday","sabtu":"saturday",
    "minggu":"sunday"
}

x = input("ketik nama hari = ").lower()
xEng = namahari[x]
print(f"bahasa ingris dari {x} = {xEng}")
y = input("Write day name = ").lower()
Yind = list(namahari.keys())[list(namahari.values()).index(y)]
print(f"bahasa indo dari {y} = {Yind}")
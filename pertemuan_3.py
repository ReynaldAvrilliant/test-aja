# angka = (input("Masukan angka berapapun = "))

# if angka[0] not in ['1', '2', '3', '4', '5', '6', '7','8', '9', '0'] : 
#     print("masukin angka goblok")
# elif angka[-1:-10] not in ['1', '2', '3', '4', '5', '6', '7','8', '9', '0'] : 
#     print("masukin angka goblok")
# elif angka[0] in ['1', '2', '3', '4', '5', '6', '7','8', '9', '0'] :
#     for angkabaru in angka:
#         if angkabaru not in ['1', '2', '3', '4', '5', '6', '7','8', '9', '0']:
#             print("masukin angka semua goblok")
#             break
#         elif angkabaru in ['1', '2', '3', '4', '5', '6', '7','8', '9', '0']:
#             angka = int(angka)
#             if(angka%2 == 0):
#                 print(angka, "merupakan angka genap")
#             elif (angka%2 != 0 ) :
#                 print(angka, "merupakan angka ganjil")
#             break
# soal solve 1
# angka = int(input("Masukan angka berapapun = "))  
# if (angka%2 == 0):
#     print("Angka ",angka, "merupakan angka genap")
# else :
#     print("angka", angka, " merupakan angka ganjil")

# soal solve 2
# BB = int(input("masukan berat badan anda (kg) = "))
# TB = float(input("masukan tinggi badan anda (m) = "))
# imt = BB/(TB**2)
# if (imt < 18.5) :
#     print("berat badan anda kurang, makan lebih banyak lagi")
# elif (imt>= 18.5 and imt<= 24.9):
#     print("berat badan anda ideal")
# elif (imt>=25 and imt<=29.9):
#     print("berat badan anda berlebih")
# elif(imt>=30 and imt<=39.9):
#     print("berat badan anda sangat berlebih")
# else:
#     print("anda obesitas")

# angka = 1
# while(angka <= 10):
#     print(angka);
#     angka+= 1

# listitem = list(range(1,11,2))
# print(listitem)
# for item in range (1,11,2):
#     print(item)

# y = "nomor urut "
# for item in range (1,11):
#     print(y+str(item))

# a = 100
# a += 1
# print(a)
# a -= 2
# print(a)
# a *= 10
# print(a)
# a **=2
# print(a)
# a//=2
# print(a)

# # list
# student = ["andi","budi","pandu","rey","bill","kampret"]
# # print(type(student))
# # print(type(student[2]))
# print(len(student))
# print(student[len(student)-1])
# print(student[0:3])
# print(student.index("budi"))
# print(student[student.index("budi")])
# print(student.count("andi"))
# print(student.index("andi"))
# print(student[0:len(student)])
# print(student[0:])
# print(student[:5])
# print(student[0:5:2])
# print(student[::2])
# print(student[::-1]) 
# print(student[::-1][0])
# print("budi" in student)
# print("budi" in student[::2])
# print("budi" in student[::1])

hari = [
    "senin","selasa","rabu","kamis","jumat","sabtu","minggu"
    ]
# hari_ditambah_100 = (hari.index("rabu")+100) % len(hari)
# hari_dikurang_100 = abs((hari.index("rabu")-100) % len(hari))
# print("100 hari setelah hari ini adalah hari: ", hari[hari_ditambah_100])
# print("100 hari sebelum hari ini adalah hari: ", hari[hari_dikurang_100])

# now = "rabu"
# hari_lagi = 5
# sisahari = abs(hari_lagi) % len(hari)
# hariygdicari = hari[(hari.index(now) + sisahari)%7]
# print(hariygdicari)

now = "rabu"
harilagi2 = -1
sisahari = harilagi2 % len(hari)
hariygdicari2 = hari[(hari.index("rabu")+sisahari)%7]
print(hariygdicari2)
bulan = [
    "januari" , "februari", "maret", "april", "mei", "juni", "juli","agustus","september","oktober","november","desember"
]

hari_ini = input("Hari ini adalah hari : ").lower()
hari_lagi = int(input("berapa hari lagi yang dicari : "))
sisahari = hari_lagi % len(hari)
hari_yang_dicari = hari[(hari.index(hari_ini)+sisahari)%7]
print(hari_lagi, " hari lagi adalah hari ", hari_yang_dicari)

bulan_ini = input("Bulan ini adalah bulan : ").lower()
bulan_lagi = int(input("berapa bulan lagi yang dicari :"))
sisabulan = bulan_lagi % len(bulan)
bulan_yang_dicari = bulan[(bulan.index(bulan_ini)+sisabulan)%len(bulan)]
print(bulan_lagi,"bulan lagi adalah bulan ", bulan_yang_dicari)
# x = [1,2,3,4,5,6,7,8,9,]
# y = range(0,100000)
# print (list(y))

# a = "purwadhika"
# b = [1,2,3]
# c = 12345
# print(list(str(c))

# y = range(0,20,2)
# y = list(y)
# print(y)
# y[0] = "andi"
# y[-1] = "kampret"
# y.append(123) #nambah dibelakang
# y.insert(0, True)
# y.insert(1, False)
# y.remove("andi")
# # y.clear() menghapus semua
# y.pop() #menghapus elemen terakhir
# y.pop(2) #menghapus index 2
# print(y)
# # y.pop(y.index("budi"))
# print(y)
# y.remove(0) #bisa dimasukin index bisa juga value
# print(y)
# print(y[::-1]) #print dari index kebelakang
# y.remove("kampret")
# y.insert(0,1)
# print(y)
# y.sort(reverse=True)
# print(y)
# y.reverse()
# print(y)

# z= "OK"
# print(z.lower())
# print(z)

angka = [52,2,4,6,7,8,9]
c = angka[0:3]
c.sort()
angka[0:3] = c
print(angka)


# a.extend(b)
# b.extend(a)


# print(a)

# a = ["apel","mangga","jeruk"]
# b = [1,2,3]
# # a,b = b,a
# a.extend(b)
# a.sort(key=lambda v:(isinstance(v,str)))
# print(a)


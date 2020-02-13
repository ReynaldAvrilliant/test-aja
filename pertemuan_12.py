# import requests
# kota = input("masukan nama kota = ")
# apikey = "cd88ef21766e13c7c197ad636d0f9ae0"
# url = f"http://api.openweathermap.org/data/2.5/weather?q={kota}&appid={apikey}"
# data = requests.get(url)
# print(data.json())

# import requests
# # jkt = 74, bali = 170,bdg = 11052
# id = 74
# cari = input("mau makan apa nih ")
# apikey = "0a3bf1038c82c32c00f9c68a130ec834"
# url = f"https://developers.zomato.com/api/v2.1/search?entity_id={id}&entity_type=city&q={cari}"

# headers = {
#     "user-key": apikey
# }

# data = requests.get(url,headers=headers)
# resto = data.json()["restaurants"]
# nomor = 1
# for i in resto:

#     print(
#         f"{nomor}",i["restaurant"]["id"],
#         i["restaurant"]["name"], ":",
#         i["restaurant"]["location"]["address"]
#         )
#     nomor +=1

# ========================================

# class dan object
# class mobil:  #CETAKAN
#     warna = "merah" #PROPERTI
#     tipe = "SUV"
# # print(mobil)
# # print(type(mobil))
# # print(mobil.warna)
# # print(mobil.tipe)
# # ====
# pajero = mobil()
# print(pajero)
# print(pajero.warna)
# print(pajero.tipe)

# agya = mobil()
# print(agya.warna)
# print(agya.tipe)

# class mobil:
#     def __init__(self,warna,tipe,seat):
#         self.warna = warna
#         self.tipe = tipe
#         self.seat = seat
#     def mahal(self):
#         if self.seat <= 4:
#             return False
#         else:
#             return True

# pajero = mobil("hitam","SUV",6)
# agya = mobil("merah","hatchback",4)
# agya2 = mobil("kuning","hatchback",4)
# print(pajero.warna,pajero.tipe,pajero.seat,pajero.mahal())
# print(agya.warna,agya.tipe,agya.seat,agya.mahal())
# print(agya2.warna,agya2.tipe,agya2.seat,agya2.mahal())

# class pizza:
#     def __init__(self,topping):
#         self.ukuran = "35"
#         self.topping = topping
#     def harga(self):
#         return len(self.topping) * 10000


# pizzaA = pizza("jagung")
# pizzaB = pizza("keju")

# print(pizzaA.ukuran,pizzaA.topping,pizzaA.harga())
# print(pizzaB.ukuran,pizzaB.topping,pizzaB.harga())

# class x:
#     y = [1,2,3,4,5]
#     z = {"nama":"andi"}
#     def luaspersegi(self, sisi):
#         return sisi**2
#     def kelilingpersegi(self,sisi):
#         return 4*sisi
# obj = x()
# print(obj.luaspersegi(12),obj.kelilingpersegi(12))
# print(obj.y[0])
# print(obj.z["nama"])

# class A:
#     def __init__(self,name,city):
        
#         self.nama = name
#         self.kota = city
# class B(A):
#     pass
# class C(A):
#     def __init__(self, name, city):
#         A.__init__(name, city)
# class D(A):
#     def __init__(self,name,city):
#         super().__init__(name,city)
# objD = D("budi","kediri")
# print(objD.nama,objD.kota)

# class manusia :
#     def __init__(self,nama):
#         self.nama = nama

# class pria(manusia):
#     def __init__(self, nama):
#         manusia.__init__(self,nama)
#         self.gender = "pria"

# class bencong(pria):
#     def __init__(self, nama):
#         pria.__init__(self,nama)
#         self.feminim = True

# class wanita(manusia):
#     def __init__(self, nama):
#         manusia.__init__(self,nama)
#         self.gender = "wanita"

# andi = bencong("andi")
# print(andi.nama,andi.gender,andi.feminim)
# fatah = wanita("fatah")
# print(fatah.nama,fatah.gender)

# class A():
#     nama = "andi"
#     def __init__(self,kota):
#         self.kota = kota

# class B(A):
#     def __init__(self, kota, prodi):
#         A.__init__(self,kota)
#         self.prodi = prodi
#     def test(self):
#         return True
# objB = B("jakarta","teknik sipil")
# print(objB.nama, objB.kota, objB.prodi)

# objA = A("jakarta")
# print(objA.nama)
# print(objA.kota) 

# print(getattr(objB,"nama"),getattr(objB,"kota"))

# print(hasattr(objB,"prodi")) #buat ngecek ada ga si prodi
# print(hasattr(objB,"alamat"))

# objB.alamat = "bsd"
# print(objB.alamat) 
# setattr(objB,"kampus","univ binus") #nambah atribut
# print(objB.kampus)

# delattr(objB,"kampus")
# print(hasattr(objB, "kampus"))
# print(vars(objB))
# print(type(vars(objB)))

# print(vars(objB).keys())
# print(list(vars(objB).keys()))
# print(vars(objB).values())
# print(list(vars(objB).values()))

# print(objB.test())

x = {
    'kota': 'jakarta',
     'prodi': 'teknik sipil',
      'alamat': 'bsd'
    }
print(x)
#bikin dict to obj
# dict to class to obj

class x():
    
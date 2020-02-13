# lucky_number = [4,8,15,29,23,42]
# friends = ["kevin", "billy", "hans", "veter", "rey", "roy"]

# friends.extend(lucky_number)
# friends.append("creed") #nambah di belakang
# friends.insert(1,"kampret")
# friends.remove("billy")

# print(friends.index("kevin"))
# print(len(friends))
# print(friends.count("kevin"))
# lucky_number.sort()
# lucky_number.reverse()
# print(lucky_number)

# friends2 = friends.copy()\

# tuple
# x= {
#     "a":"andi",
#     "b":"budi",
#     "c":"caca"
# }
# print(x.get("a"))
# print(x.get("d", "maaf data tidak ditemukan"))
# x = {"senin":"monday","selasa":"tuesday"}
# keys = list(x.keys())
# vals = list(x.values())
# print(keys)
# keys[keys.index("senin")] = 1
# print(keys)

# namahari = {
#     "senin":"monday","selasa":"tuesday","rabu":"wednesday",
#     "kamis":"thursday","jumat":"friday","sabtu":"saturday",
#     "minggu":"sunday"
# }
# x = input("masukan nama hari : ").lower()
# y = namahari.get(x,"maaf tulisan anda salah")
# print(f"bahasa inggrisnya  {x} = {y}" )
# x = input("masukan hari dalam bahasa inggris = ").lower()
# for day in namahari.keys():
#     if x in namahari.get(day):  
#         y = day
# print(f"bahasa indonesianya {x} = {y}")


# angka = {
#     "satu":"one","dua":"two","tiga":"three","empat":"four",
#     "lima":"five","enam":"six","tujuh":"seven","delapan":"eight",
#     "sembilan":"nine","sepuluh":"ten"
# }
# x = input("masukan angka dalam bentuk tulisan = ").lower()
# y = angka.get(x,"maaf tulisan anda salah")
# print(f"bahasa inggris {x} = {y}")
# keys = list(angka.keys())
# vals = list(angka.values())
# angka = dict(zip(vals,keys))
# x = input("masukan nama angka dalam bahasa inggris = ").lower()
# y = angka.get(x,"tulisan anda salah")
# print(f"Bahasa inggris dari {x} = {y}")

# Tuple in tuple
a = ((1,2),(3,4),(5,6),(7,8))
# soal (3,4),(1,2),(7,8),(5,6)
ax= list(a)
ax[0] = list(a[0])
ax[1] = list(a[1])
ax[2] = list(a[2])
ax[3] = list(a[3])
print(ax)
ax[0][0],ax[0][1] = ax[0][1],ax[0][0]
ax[1][0],ax[1][1] = ax[1][1],ax[1][0]
ax[2][0],ax[2][1] = ax[2][1],ax[2][0]
ax[3][0],ax[3][1] = ax[3][1],ax[3][0]
ax[0] = tuple(ax[0])
ax[1] = tuple(ax[1])
ax[2] = tuple(ax[2])
ax[3] = tuple(ax[3])
ax = tuple(ax)
print(ax)

az = list(a)
az[0],az[1] = az[1],az[0]
az = tuple(az)
print(az)
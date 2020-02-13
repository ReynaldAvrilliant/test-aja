# A = set(range(2,20,2))
# B = set(range(1,20,2))
# C = set(range(1,-10,1))
# A = {2,4,6,8,10,12,14,16,18}
# B = {3,5,7,9,11,13,15,17,19}
# C = {-9,-8,-7,-6,-5,-4,-3,-2,-1}
# D = {2,3,5,7,11,13,17,19}
# E = {4,6,8,9,10,12,14,15,16,18}
# # A U B U C U D U E
# print(A|B|C|D|E)
# print(A.union(B,C,D,E))
# # (A n B) U (D n E)
# print((A&B)|(D&E))
# print((A.intersection(B).union(D.intersection(E))))
# # (A u B) N (D u E)
# print((A.union(B).intersection(D.union(E))))
# print((A|B)&(D|E))
# # (A u B) - (D u E)
# print((A|B)-(D|E))
# print((A.union(B).difference(D.union(E))))
# # (A u B u C) - (A n E)
# print((A.union(B,C).difference((A.intersection(E)))))
# print((A|B|C)-(A&E))


# bisa di tambah dengan add dan update 
# kalo update nambahnya per elemen
# kalo add nambah semua

A = {1,2,3}
A.add ("budi")
A.add(("a","b","c"))
print(A)
A.update((4,6,5))
A.update("Caca")
A.update([8,9,7])
print(A)
# A.remove(1) #harus 1 1
# print(A)
# # A.clear()
# # print(A)
# # A.pop()
# # print(A)
A.discard(("a","b","c"))
# print(A)

# # set immutable
# # frozen set tidak bisa di apa apa in
# x = {1,2,3,4,5}
# print(type(x))
# y = frozenset(x)
# print(y)
# print(type(y))

# y.add("budi")
# print(y)

# x = {1,2,3}
# # x.remove(4) #eror karena lapor
# x.discard(4) #ga eror karna dia cuma berfungsi kalo ada
# print(x)

# sangat bermanfaat " dictonary " pakai {key:value}
# x= {
#     "a":"andi",
#     "b":"budi",
#     "c":"caca"
# }

# # print(type(x))
# # print(x["a"])
# # print(x["c"])
# # print(x.get("a"))
# # print(x.get("d", "maaf data tidak ditemukan"))
# x["a"] = "budi"
# x["kota"] = "jakarta" #buat nambah
# print(x)
# x.update({"b":"toyoya"}) #ganti baru valuenya
# x.update({"f" : "deni", "g" : "susi"})
# print(x)
# x.pop("kota") #ngapus sama key value
# print(x)
# del x["a"]
# print(x)

# # untuk tau siapa aja key nya
# print(list(x.keys()))
# print(list(x.values()))

# a = [1,2,3]
# b = ["andi", "budi" , "caca"]

# c = (zip(a,b))
# d = dict(c)
# print(d)

# x = {"senin":"monday","selasa":"tuesday"}
# keys = list(x.keys())
# vals = list(x.values())
# print(keys)
# keys[keys.index("senin")] = 1
# print(keys)

# d = dict(zip(keys,vals))
# print(d)
namahari = {
    "senin":"monday","selasa":"tuesday","rabu":"wednesday",
    "kamis":"thursday","jumat":"friday","sabtu":"saturday",
    "minggu":"sunday"
}

x = input("masukan nama hari : ").lower()
y = namahari.get(x,"maaf tulisan anda salah")
print(f"bahasa inggrisnya  {x} = {y}" )
keys = list(namahari.keys())
vals = list(namahari.values())
namahari = dict(zip(vals,keys))
x = input("masukan hari dalam bahasa inggris = ").lower()
y = namahari.get(x,"maaf tulisan anda salah")
print(f"bahasa indonesianya {x} = {y}")

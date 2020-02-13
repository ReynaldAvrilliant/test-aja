# # first
# x = [
#     [1,2,3,4],
#     [5,6,7,8]
#     ]
# print(len(x))
# print(x[0])
# print(x[1])
# print(x[0][0])
# print(x[1][2])
# print(x+x)
# print([x])
# y = [x]
# print(y)
# print(y[0][1][0])
# print([y[0][0][0],y[0][1][1]])
# print([y[0][0][2],y[0][1][0]])
# end

# tuple immutable
# 2
# x=(1,2,3,4,5)
# y=[1,2,3,4,5]
# y[0] = "andi"
# print(y)
# # x[0] = "andi"
# # print(x) #eror karena tuple tidak bisa di ubah dan tidak bisa di tambah dll
# print(type(x))
# print(x[0::2]) #2 itu stepnya 0 start
# # print(list(x)) #mengubah tuple jadi list
# y = list(x)
# y[0] = "andi"
# x = tuple(y) #mengubah x jadi lis dan mengubah lagi menjadi tuple
# print(x)
# print("andi" in x)
# print("budi" in x)
# a = ((1,2),(3,4),(5,6),(7,8))
# print(a[0])
# print(a[1][1])
# print((a[1],a[0],a[3],a[2]))
# a = list(a)
# a[0],a[1]=a[1],a[0]
# a[2],a[3]=a[3],a[2]
# a = tuple(a)
# print((a))
# 1,3 . 2,4 . 5,7. 6,8 soal
# print((((a[0][0]),a[1][0]))((a[0][1]),a[1][1]))(((a[2][0],a[3][0])))((a[2][1],a[3][1]))

# x= ("andi") #ga pake koma dianggap str
# print(type(x)
# print(x+"g")
# print(x[0])

# x("andi",) #pake koma di anggap tuple
# print(type(x)) 

# x=(1,2,3) #tuples cuma bisa di tambah dengan tuples

# print(x+x)
# print(x*5)
# print( 1 in x) #in sama not in bisa juga di list ga harus di tuples
# print( 1 not in x)
# del x
# print(x)

# 3
# x = [
#     (1,["a","b"]),
#     (3,4)
#     ]
# x[0][1][0] = "andi"
# print(x)
## set untuk himpunan {} 
## bisa mengubah tuple dan list ke set#
# #  elemen set unik
# x = {1,2,3,3,2,1,"andi"}
# # print(x[0]) #gabisa karena x tidak ada index ga punya index, ga ngaruh urutan
# print(x)
# print(len(x))
# print(type(x))


# x = [1,2,3,4,1,2,3]
# y = tuple(x)
# za = set(x)
# zb = set(y)
# print(za)
# print(zb)
# #set itu bisa di ubah di update dikurangi, elemen harus immutable
# #elemen di dalamnya tidak bisa di ganti jadi list tidak bisa di dalam set dan tidak bisa di ganti
# # set tidak dapat di set.sort
# y = {1,2,(5,6)}
# print(y)
# print(1 in y)
# print(len(y))

a = {1,2,3,}
b = {3,4,5,6}
# a U b

# print(a | b)
# print(a.union(b))

# intersection irisan n
# print(a&b)
# print(a.intersection(b))

# # #difference a-b
# print(a-b)
# print(a.difference(b))

# # simetrik difference
print(a ^ b)
print(a.symmetric_difference(b))

# a U b

# {1,2,3,4,5,6}
# a n b
# {3}
# a - b (dif) hanya ada di a
# {1,2}
# simetrik difference 
# {1,2,4,5,6}


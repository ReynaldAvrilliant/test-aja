# lambda function
# a = lambda c : c**2 # : adalah return
# print(a(4))

# def x(d):
#     return d ** 2
# print (x(2))

# a = lambda x : "genap" if x%2 == 0 else "ganjil"
# print(a(2))

# def b(x):
#     if x%2 ==0:
#         return "genap"
#     else:
#         return "ganjil"
# print(b(2))

# def f(x):
#     return lambda a : a**x
# pangkat2 = f(2)#x
# pangkat3 = f(3)
# print(pangkat2(3)) #a
# print(pangkat3(3))
# print(f(2)(3))



# x = [1,2,3,4,5]
# # lambda function, print setiap elemen x
# def z(a):
#     return[print(i)for i in x] #best
# z(x)

# y = lambda a : [print(i)for i in a]
# y(x)
# def b(c):
#     for i in c:
#         print(i) #good way
# b(x)


# x = [1,2,3,4,5]
# # for i in x:
# #     print(i)

# y = [print(i) for i in x]
# y


# s = lambda :5

# print(s())

# listku = [
#     lambda:1,
#     lambda:2,
#     lambda:[4,5,6]
# ]
# print(listku[0]()) #cara manggil
# print(listku[2]()[1]) #5
# a = lambda:4
# print(a())

# map filter reduce
# x = [1,2,3,4,5]
# def y(a):
#     return a
# print(y(x))
# b = map(y,x)
# print(list(b))

# x = [1,2,3,4,5]
# y = []
# for i in x:
#     i += i #pake loop
#     y.append(i)
# print(y)


# x = [1,2,3,4,5]
# def jumlah(i):
#     return i+i  #pake map

# y = map(jumlah,x)
# print(list(y))


# x = [1,2,3,4,5]
# y = map(lambda a: a + a,x) #cara lain
# print(list(y))


# x = [1,2,3,4,5]
# y = map(lambda a: a**3,x)
# print(list(y))

# w = [2,2,2,2,2]
# x = [1,2,3,4,5]
# y = [5,4,3,2,1]
# def jumlah (i,j,K):
#     return i+j+K

# z = map(jumlah,x,y,w)
# print(list(z))

# w = [2,2,2,2,2]
# x = [1,2,3,4,5]
# y = [5,4,3,2,1]
# def pangkat (i,j):
#     return i**j
# z = map(pangkat,x,y)
# print(list(z))

# filter harus true or false
# x=[3,5,7,4,8,9,2]
# y=[]
# for i in x:
#     if i > 4:
#         y.append(i)
# print(y)

# def lebih4(i):
#     if i > 4:
#         return True
#     else:
#         return False
# z = filter(lebih4,x)
# print(list(z))
# a = filter(lambda i: True if i> 4 else False,x)
# print(list(a))
# b = filter(lambda i:i > 4,x )
# print(list(b))

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [1,2,12,4,5,13,7,8,19,10]
# # z = list(set(x).intersection(y))
# # print(z) #tanpa filter
# def sama (i):
#     if i in set(x)&set(y):
#         return True
#     else:
#         return False
# z = filter(sama,y)
# print(list(z)) # cara 1
# d = filter(lambda a:a in set(x)&set(y),y)
# print(list(d)) # cara 2
# w = filter(lambda i:i in x,y)
# print(list(w)) #cara 3
# ============================================
# data = list(range(0,103))
# def prima(x):
#     if x > 1:
#         if x == 2:
#             return True
#         else:
#             for i in range (2,x):
#                 if x%i == 0:
#                     return False
#             return True
                
#     else:
#         return False
# z = list(filter(prima,data))
# print(z)
# =========================
# def x():
#     return "ok"
#     print("tes")
# print(x())
# x()
# =========================
# reduce buat nambah semua
# angka = [1,2,3,4,5]
# from functools import reduce
# z = reduce(lambda x, y: x+y, angka)
# print(z)
# z = reduce(lambda x, y: x*y, angka)
# print(z)

# print(max(angka))
# print(min(angka))
# # ========================
# i=1
# while i < 6:
#     print(i)
#     if i == 3:
#         break
#     i+=1

# # ======================
# i = 0
# while i<6:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
x = [1,2,3,4,5]

a = filter(lambda i: i%2==0,x)
b = map(lambda i:i ** 2, list(a))
print(list(b))

c = list(map(lambda i : i**2, filter(lambda j : j%2==0, x)))
print(list(c))


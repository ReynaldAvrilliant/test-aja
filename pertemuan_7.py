# x = "aliando" #jadiin aloandi
# i = 0
# while i <= len(x):
#     print(x[i]) 
#     i += 1

# x = "aliando"
# i = 0
# while i<len(x):
#     if x[i]=="i":
#         x = x[:i] + "o" + x[i+1:]
#     elif x[i] =="o":
#         x  = x[:i] + "i" + x[i+1:]
#     i+=1

# print(x)
    
# x = [ 
#     {"Nama" : "Andi","kota":"bsd"},
#     {"Nama" : "budi","kota":"jakarta"},
#     {"Nama" : "caca","kota":"bandung"}
# ]
# i=0

# while i < len (x):
#     print(x[i]["Nama"])
#     i+=1
# j=0
# while j < len(x):
#     print(x[j]["kota"])
#     j+=1

# x = [1,2,3,4,5]
# for elemen in x:
#     print(elemen)
# for i in x:
#     print(i)
# for i in range(1,10,2):
#     print(f"index ke {i}")

# nama = ["andi", "budi", "caca"]
# for name in nama:
#     print(f"{nama.index(name)+1}-{name}")

# for num in range(20):
#     if num % 2 == 0:
#         print(num)

# for num in range (0,20,2):
#     print(num)
# for num in range (10,0,-1):
#     print(num)

# def fizbuzz(jarak):

#     for num in range (1,jarak+1):
#         if num % 3 == 0 and num % 5 != 0:
#             print("fizz")
#         elif num % 5 == 0 and num % 3 != 0:
#             print("buzz")
#         elif num %3 == 0 and num%5 == 0:
#             print("fizzbuzz")
#         else:
#             print(num)
# fizbuzz(100)

# a = ["a","b,","c","d"]

# a.reverse()
# print(a)

# print(a[::-1]) #ngebalik
# print(list(reversed(a)))


# def balik (x):
#     y = []
#     for i in range(len(x)):
#         y.insert(0,x[i])
#     return y
# print balik([1,2,3])

# def balik2(x):
#     for i in range(round(len(x)/2)):
#         y=x[i]
#         x[i] = x[len(x)-1-i]
#         x[len(x)-1-i] = y
#     return x
# print(balik2([1,2,3]))


# x**y pakai function and for

# def pangkat (x,y):
#     hasil = 1
#     for i in range (y):
#         hasil = hasil * x
#     return hasil

# print(pangkat(3,3))

# def pangka2(x,y):
#     if y == 1:
#         return x
#     else:
#         return x * pangkat(x,y-1)
# print(pangka2(2,3))

# star = ""
# for i in range(5):
#     star += str(i+1) + " "
#     print(star)

# x = ""
# for i in range(10):
#     for j in range(i):


# x = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# for i in range (len(x)):
#     for j in range (len(x[i])):
#         print(x[i][j])

# for row in x:
#     for col in row:
#         print(col)

star = ""
for i in range(5,0,-1):
    for j in range(i):
        star += " * "
    star += "\n"
print(star)


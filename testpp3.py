# angka = 1
# while(angka<=100):
#     print(angka)
#     angka +=2

# listitem = list(range(1,12,2))
# print(listitem)

# for item in range (1,12,2):
#     print(item)

# y = "nomor urut "
# for item in range (1,10,1):
#     print(y + str(item))

# y = "nomor absen "
# for item in range(1,20,2):
#     print(y + str(item))

# y = "nomor urut "
# for item in range(1,21,2):
#     print(y + str(item))

# z = ""
# for item in range(0,5):
#     z +=" * "
# print(z)

# z = ""
# for item in range (0,5):
#     z += " * \n"
# print(z)

# z=""
# for item in range(5):
#     for item in range(5):
#         z += "*"
#     z += "\n"
# print(z)

# z = ""
# for item in range (2):
#     for item in range (5):
#         z +="*"
#     z+= "\n"
# print(z)

# z = ""
# for item in range (5):
#     for item in range (0, item+1):
#         z +="*"
#     z+="\n"
# print(z)


# z = ""
# for item in range (5,0,-1):
#     for item in range (0, item):
#         z +="* "
#     if(item==0):
#         z+=""
#     elif (item>0):
#         z+="\n"
# print(z)
# z = ""
# for item in range (1,5):
#     for item in range (item+1):
#         z +="* "
#     z+="\n"
# print(z)

z = ""
for item in range (0,5):
    z += " * "
print(z)

z = ""
for i in range (5):
    z+= " * \n"
print(z)

# z = ""
# for item in range (0,5):
#     for j in range (0,5):
#         z+= " * "
#     z+= "\n"
# print(z)
# z = ""
# for i in range (5,0,-1):
#     for j in range(0,i):
#         z+= " * "
#     if i==1:
#         z+=""
#     else:
#         z+= "\n"
# print(z)
# z=""
# for i in range (1,5,1):
#     for j in range (0,i+1):
#         z+=" * "
#     z+="\n"
# print(z)
# ============
h = int(input("please enter diamond height = "))
for i in range(h):
    print(" "*(h-i),"*"*(i*2+1))
for i in range (h-2, -1, -1):
    print(" "*(h-i),"*"*(i*2+1))

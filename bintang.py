# baris = 5
# z=""
# for i in range(baris):
#     for j in range(i,baris-1):
#         z+=" "
#     for k in range(2*i+1):
#         z+="*"
#     z+="\n"
# print(z)

# baris = 5
# z=""
# for i in range(baris):
#     for j in range(i):
#         z+=" "
#     for k in range(2*(baris-i)-1):
#         z+="*"
#     z+="\n"
# print(z)

# ==diamond

# baris = 5
# z=""
# for i in range(baris):
#     for j in range(i,baris-1):
#         z+=" "
#     for k in range(2*i+1):
#         z+="*"
#     z+="\n"
# for i in range(baris):
#     for j in range(i):
#         z+=" "
#     for k in range(2*(baris-i)-1):
#         z+="*"
#     z+="\n"
# print(z)


# n = 5
# z=""
# for i in range(n):
#     for j in range(i,n-1):
#         z+=" "
#     for k in range(2*i+1):
#         z+="*"
#     z+="\n"
# for i in range(n):
#     for j in range(i):
#         z+=" "
#     for k in range(2*(n-i)-1):
#         z+="*"
#     z+="\n"
# print(z)


# n = int(input("baris segitiga = "))
# z=""
# for i in range(n):
#     for j in range(i,n-1):
#         z+=" "
#     for k in range(2*i+1):
#         z+="*"
#     z+="\n"
# print(z)
# for i in range(n):
#     for j in range(i):
#         z+=" "
#     for k in range (2*(n-i)-1):
#         z+="*"
#     z+="\n"
# print(z)

string = input("input kata = ")
length = len(string)
for row in range(length):
    for col in range (row+1):
        print(string[col],end="")
    print()
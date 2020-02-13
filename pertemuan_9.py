myfile=open("./txt/pertemuan_9.txt","r")
# 1
# print(myfile)
# print(myfile.readable())
# print(myfile.read())
# print(myfile.readlines())
# print(myfile.readline())
# 2
# x = list(map(lambda i: i,myfile.readlines()))
# print(x)
# 3
# for i in myfile.readlines():
#     print(i.replace("\n","")) # .replace("\n","") ngilangin enter

# =========================================
# myfile = open("pertemuan_9.csv","r")
# # print(myfile.readlines())
# data = []
# for i in myfile.readlines()[1:]:
#     no = int(i.split(";")[0])
#     nama = i.split(';')[1].replace('\n','')
#     x = {"no":no,"nama":nama}
#     data.append(x)
# print(data)
# nama = input("ketik nama = ")
# new = {"no":data[-1]["no"]+1,"nama":nama}
# data.append(new)
# print(data)

# myfile = open("pertemuan_9.csv","w")
# myfile.write("no;nama\n")
# myfile = open("pertemuan_9.csv","a")
# for i in data:
#     myfile.write(
#         f'{i["no"]};{i["nama"]}\n'
#     )
# =========================================
print("welcome, pilih menu = ")
print("1. signup ")
print("2. login ")
opsi = input("ketik opsi (1/2) = ")
if opsi =="1":
    ketik_nama = input("ketik nama = ")
else:
    ketik_no = input("masukan nomor urut = ")
    ketik_nama1= input("masukan nama = ")
if opsi =="2":
    myfile = open("pertemuan_9.csv","r")
    noInput = input("masukan no = ")
    listnomor = []
    listnama = []
    for i in myfile.readlines()[1:]:
        no = i.split(";")[0]
        nama = i.split(";")[1].replace("\n","")
        listnomor += [no]
        listnama += [nama]
    if noInput in listnomor:
        namaInput = input("ketik nama = ")
        noInputIndex = listnomor.index(noInput)
        if namaInput == listnama[noInputIndex]:
            print("LOGIN BERHASIL")
        else:
            print("login gagal")
    else:
        print("login gagal")

myfile = open("pertemuan_9.csv","r")
for i in myfile.readlines()[1:]:
    no = int(i.split(";")[0])
no+=1

# myfile = open("pertemuan_9.csv", "a")
# myfile.write(f"{no};{ketik_nama}\n")
# print("anda terdaftar dengan nomor ", no)
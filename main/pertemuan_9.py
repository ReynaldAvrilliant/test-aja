myfile=open("./../txt/pertemuan_9.txt","r") #./../ buat keluar dr folder
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
for i in myfile.readlines():
    print(i.replace("\n","")) # .replace("\n","") ngilangin enter
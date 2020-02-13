# myjson = open("11.json","r")
# # print(myjson.readable()) #buat ngebaca file
# myjson = (myjson.readlines())
# print(myjson)

# import csv

# with open ("pertemuan_9.csv","r") as mycsv:
#     reader = csv.reader(mycsv)
#     print(reader)
#     print(list(reader))

# ngebaca csv
# data =[]
# with open ("pertemuan_9.csv","r") as mycsv:
#     reader = csv.DictReader(mycsv, delimiter = ",")
#     for i in reader:
#         data.append(dict(i))

# print(data)

# menulis csv
# with open ("pertemuan_9.csv","w") as mycsv:
#     writer = csv.writer(mycsv, delimiter=",")
#     writer.writerow([13,"rudi"]) #masukin satu data .writerows masukin byk data

# with open ("pertemuan_9.csv","a", newline="") as mycsv:
#     writer = csv.writer(mycsv, delimiter=",")
#     writer.writerow([13,"rudi"])

# with open ("pertemuan_9.csv","a", newline="") as mycsv:
#     writer = csv.writer(mycsv, delimiter=",")
#     writer.writerows([[13,"rudi"],[14,"bebi"],[15,"gilang"]])

# with open ("pertemuan_9.csv","a", newline="") as mycsv:
#     writer = csv.DictWriter(
#         mycsv, delimiter=",",fieldnames=["no","nama"])
#     writer.writerow({"no":33,"nama":"dedi"})

# with open ("pertemuan_9.csv","a", newline="") as mycsv:
#     writer = csv.DictWriter(
#         mycsv, delimiter=",",fieldnames=["no","nama"])
#     writer.writerows([
#         {"no":61, "nama":"handi"},
#         {"no":62, "nama":"hadi"},
#         {"no":63, "nama":"hani"}
#     ])

import json
# with open("11.json","r") as myjson:
#     data = json.load(myjson)

# print(data)
x = [
    {"nama":"ali","kota":"BSD"},
    {"nama":"BUDI","kota":"BALI"},
    {"nama":"WONI","kota":"JAKARTA"}
]

with open("11.json","w") as myjson:
    json.dump(x,myjson)
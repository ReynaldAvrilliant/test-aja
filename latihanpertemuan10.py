# import csv
# with open("10.csv","r") as mycsv:
#     reader = csv.reader(mycsv)
#     print(reader)
#     print(list(reader))

# import csv
# import json #csv to json
# data = []
# with open("10.csv","r") as mycsv:
#     reader = csv.DictReader(mycsv,delimiter=",")
#     for i in reader:
#         data.append(dict(i))
# print(data) 

# with open("11.json","w") as myjson:
#     json.dump(data,myjson)


import json 
import csv 
with open("lat10.json","r") as myjson: #buat ngeload data dari json
    data = json.load(myjson) #buat ngeload data dari json
print(data)

with open("jsontocsv.csv","w") as mycsv1:
    writer = csv.DictWriter(mycsv1, delimiter=",",fieldnames=["id","nama","Kota"]) #write ke csv,tapi udah harus dalam 
    writer.writerows(data)

# import csv
# import json #csv to json
# data = []
# with open("pr10.csv","r") as mycsv:
#     reader = csv.DictReader(mycsv,delimiter=";") #akan read csv dalam bentuk list of dictionary, karna json harus list of dict
#     for i in reader:
#         data.append(dict(i))
# print(data) 

# with open("12.json","w") as myjson:
#     json.dump(data,myjson)
# =========================================json to csv
# import json 
# import csv 
# with open("12.json","r") as myjson: #buat ngeload data dari json
#     data = json.load(myjson) #buat ngeload data dari json
# print(data)

# with open("11.csv","w") as mycsv1:
#     writer = csv.DictWriter(mycsv1, delimiter=",",fieldnames=["no","nama","kota"]) #write ke csv,tapi udah harus dalam 
#     writer.writerows(data)

# ==========================================csv to xlxs
import xlrd #buat baca
pr10 = xlrd.open_workbook("pr10.xlsx")
sheet = pr10.sheet_by_name("pr10")
no = []
nama = []
kota = []
for i in range(1,sheet.nrows):
    no.append(sheet.cell_value(i,0))
    nama.append(sheet.cell_value(i,1))
    kota.append(sheet.cell_value(i,2))  

print(no,nama,kota)
data = list(zip(no,nama,usia,kota))
print(data)
data = []
for i in range(1,sheet.nrows):
    new = []
    for j in range(sheet.ncols):
        new.append(sheet.cell_value(i,j))
    data.append(tuple(new))
print(data)
    
print(data)
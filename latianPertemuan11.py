# json to csv
import requests
import json 
import csv 
url = "http://jsonplaceholder.typicode.com/users"
data = requests.get(url)
hasil = data.json()
# with open("14.json","r") as x: #buat ngeload data dari json
#     data = json.load(x) #buat ngeload data dari json
#     json.dump(hasil,x)
print(hasil)

# with open("14.csv","w") as mycsv1:
#     writer = csv.DictWriter(mycsv1, delimiter=";",fieldnames=["id","name","username","email","address","street","suite","city","zip","geo","lat","long"]) #write ke csv,tapi udah harus dalam 
#     writer.writerows(data)
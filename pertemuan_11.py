# # request API to server backend ke database
# # web scraping = belajar HTML
# # database : rdbms (table) & non rdbms (non table)

# # happycoding
# # GET request Rest API
# import requests
# url = "http://jsonplaceholder.typicode.com/users"
# data = requests.get(url)
# # print(data)
# hasil = data.json()
# # print(hasil[0]["name"])
# # for i in hasil: #cuma buat nama
# #     print(i["name"])
# for i in hasil:
#     print(i)

# ===========================================
# untuk menjadikan json dr API
# import requests
# import json
# url = "http://jsonplaceholder.typicode.com/users"
# data = requests.get(url)
# hasil = data.json()
# with open('13.json','w') as x:
#     json.dump(hasil,x)

# # =========================================
# import requests
# import json
# url = "http://jsonplaceholder.typicode.com/users"
# data = requests.get(url)
# if data.status_code == 200:
#     hasil = data.json()
#     print(hasil[0]["address"]["street"])
# else:
#     print("request tidak sukses")

# 
# import requests
# url = "http://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p="
# nama = input("ketik nama atlit = ")
# data = requests.get(url + nama)
# if data.status_code == 200:
#     hasil = data.json()
#     print(hasil["player"][0]["strTeam"])
# else:
#     print("request tidak sukses")

import requests
url = "http://kurs.web.id/api/v1/"
kode_bank = input("masukan kode bank = ")
data = requests.get(url + kode_bank)
if data.status_code == 200:
    hasil = data.json()
    konversi = input("Jika ingin mengkonversi USD to IDR (1) / IDR to USD (2)= ")
    if konversi == "1":
        jumlahusd = int(input("masukan jumlah USD yang ingin anda konversi ke rupiah = "))
        konversi_USDIDR = int(hasil["beli"])*jumlahusd
        print(jumlahusd, " USD = Rp. ", konversi_USDIDR)
    else:
        jumlahrupiah = int(input("masukan jumlah IDR yang ingin anda konversi ke USD = "))
        konversi_IDRUSD = jumlahrupiah/int(hasil["jual"])
        print(jumlahrupiah," IDR = " ,konversi_IDRUSD, " USD")
else:
    print("request tidak sukses")
'''
- request API => server backend => database
- web scraping ( data di website tidak bisa download, tidak ada api. ada syarat dan ketentuan untuk dapat dilakukan) => HTML
tutorial HTML : w3schools.com, youtube : lintang wisesa, developer.mozilla.org
- database rdbms (tabel) dan non rdbms (non tabel)
beberapa program yang digunakan untuk membuat tampilan website (untuk proyek akhir)
- <HTML> (fondasi)
- <CSS> (Mempercantik)
- <javascript> (fasilitas)

protocol : http
method : get

try : https://jsonplaceholder.typicode.com/
untuk nge get API bisa langsung dibrowser asalkan tau routenya
software untuk ngetest API : postman (download appnya, install)
API :https://jsonplaceholder.typicode.com/users
https://jsonplaceholder.typicode.com/users/1 , keluar 1 user aja disebut dynamic roots
untuk kode : bisa cek di http status code

kalau main twitter cari happycoding => vscode

package
pip install / py -m pip install
pip uninstall/ py -m pip uninstall
pip list/ py -m pip list
pip install -- upgrade / py -m pip install --upgrade
pip install pacakge==versi
'''

# GET request REST API

import requests # install dulu
url = 'https://jsonplaceholder.typicode.com/users'
data = requests.get(url)
print(data) #ketika response 200 ok artinya valid baru tanya datanya
if data.status_code == 200 : #ketika response 200 ok artinya valid baru tanya datanya
    hasil = data.json()
    print(hasil)
    print(hasil[0]) #atau bisa juga getnya ke users/1
    print(hasil[0]['name']) #ketika ingin diambil datanya saja
    for i in hasil :
        print(i['name'])

    # dari data yang ada ingin dibuat dalam bentuk json
    import json
    with open ('14.json','w') as myjson :
        json.dump(hasil, myjson)

    # dari data yang ada ingin dibuat dalam bentuk CSV dan excel
    # id name username email adress (street,suite,city,zip), geo(lat,long), phone, web, company(name)
    # dalam bentuk csv
    import csv
    with open('14.csv','w',) as mycsv :
        writer = csv.DictWriter(mycsv, delimiter =';', fieldnames = ['id','name','username','email','address','geo','website','phone','company'])
        writer.writerows([{'id':'id','name':'name','username':'username','email':'email','address':'address','geo' : 'geo','website':'website','phone':'phone','company':'company'}])
        writer.writerows(hasil)
    # dalam bentuk excel
    import xlsxwriter
    book = xlsxwriter.Workbook("14.xlsx")
    sheet = book.add_worksheet("Database")
    row = 1
    sheet.write(0,0, "id")
    sheet.write(0,1, "name")
    sheet.write(0,2, "username")
    sheet.write(0,3, "email")
    sheet.write(0,4, "address")
    sheet.write(0,5, "geo")
    sheet.write(0,6, "phone")
    sheet.write(0,7, "web")
    sheet.write(0,8, "company")
    for i in range(0, len(hasil)) :
        sheet.write(row,0, hasil[i]['id'])
        sheet.write(row,1, hasil[i]["name"])
        sheet.write(row,2, hasil[i]["username"])
        sheet.write(row,3, hasil[i]["email"])
        sheet.write(row,4, (hasil[i]["address"]['street'] + "," + hasil[i]["address"]['suite'] + "," + hasil[i]["address"]['city'] + "," + hasil[i]["address"]['zipcode']))
        sheet.write(row,5, (hasil[i]["address"]["geo"]['lat'] + ","+ hasil[i]["address"]["geo"]['lng']))
        sheet.write(row,6, hasil[i]["phone"])
        sheet.write(row,7, hasil[i]["website"])
        sheet.write(row,8, hasil[i]["company"]['name'])
        row += 1
    book.close()
# else :
#     print("Request tidak sukses")
'''
TheSportsDB : untuk data pemain dkk free
kurs.web.id
'''
# url = "https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?p="
# nama = input ("Ketik nama Atlet : ")
# data = requests.get(url+nama)

# if data.status_code == 200 :
#     hasil = data.json ()
#     print(hasil['player'][0]['strTeam'])
# else :
#     print ("Request tidak sukses")

# url = "https://kurs.web.id/api/v1/bca"
# data = requests.get(url)
# if data.status_code == 200 :
#     hasil = data.json ()
#     print(hasil)
# else :
#     print ("Request tidak sukses")


# namabank = input('Masukan nomor bank yang anda inginkan untuk di cek kursnya : \
#                  \nPilihan bank : \
#                  \n1. BCA\n2. BI\n3. BJB\n4. BNI\n5. BRI\n6. BTN\n7. BUKOPIN\n8. CIMB\n9. COMMONWEALTH \
#                  \n10. DANAMON\n11. HSBC\n12. JTRUST\n13. MANDIRI\n14. MAYAPADA\n15. MAYBANK \
#                  \n16. MEGA\n17. MUAMALAT\n18. OCBC\n19. PANIN\n20. PERMATA\n21. SINARMAS\n22. UOB \
#                  \n23. WOORISAUDARA \nMasukan pilihan anda : ')
# if namabank == '1':
#     namabank = 'bca'
# elif namabank == '2':
#     namabank = 'bi'
# elif namabank == '3':
#     namabank = 'bjb'
# elif namabank == '4':
#     namabank = 'bni'
# elif namabank == '5':
#     namabank = 'bri'
# elif namabank == '6':
#     namabank = 'btn'
# elif namabank == '7':
#     namabank = 'bukopin'
# elif namabank == '8':
#     namabank = 'cimb'
# elif namabank == '9':
#     namabank = 'commonwealth'
# elif namabank == '10':
#     namabank = 'danamon'
# elif namabank == '11':
#     namabank = 'hsbc'
# elif namabank == '12':
#     namabank = 'jtrust'
# elif namabank == '13':
#     namabank = 'mandiri'
# elif namabank == '14':
#     namabank = 'mayapada'
# elif namabank == '15':
#     namabank = 'maybank'
# elif namabank == '16':
#     namabank = 'mega'
# elif namabank == '17':
#     namabank = 'muamalat'
# elif namabank == '18':
#     namabank = 'ocbc'
# elif namabank == '19':
#     namabank = 'panin'
# elif namabank == '20':
#     namabank = 'permata'
# elif namabank == '21':
#     namabank = 'sinarmas'
# elif namabank == '22':
#     namabank = 'uob'
# elif namabank == '23':
#     namabank = 'woorisaudara'
# else :
#     print('Maaf nama bank yang anda masukan salah !')
# url = "https://kurs.web.id/api/v1/"
# data = requests.get(url+namabank)
# if data.status_code == 200 :
#     hasil = data.json ()
#     print('Berikut harga beli dan jual mata uang di bank '+hasil['bank']+' dengan mata uang '+hasil['matauang'])
#     print('Harga beli : '+hasil['beli'])
#     print('Harga beli : '+hasil['jual'])

# jualBeli = input('Masukan pilihan transaksi anda : (1. Beli/2. Jual) \n')
# if jualBeli == '1':
#     masukanNominal = input('Masukan nominal IDR yang ingin anda konversi USD : ')
# if jualBeli == '2':
#     masukanNominal = input('Masukan nominal USD yang ingin anda konversi IDR : ')
# if jualBeli == '1':
#     hasilConvert =  int(masukanNominal) / int(hasil['jual'])
#     print(f'USD yang akan anda dapatkan adalah {hasilConvert}')
# elif jualBeli == '2':
#     hasilConvert = int(hasil['beli']) * int(masukanNominal)
#     print(f'Rupiah yang akan anda dapatkan adalah {hasilConvert}')

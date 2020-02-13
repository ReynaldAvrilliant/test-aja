# import ztest
# print(x.nama)
# print(x.tesfunc("budi"))

# objA = x.A()
# print(objA.nama)
# =============================
# import ztest #1
# from ztest import jsonku #cara 2
# x = jsonku("z.json")
# print(x.buka())
# ======================

# import datetime
# x=datetime.datetime.now()
# print(x)
# print(x.year)
# print(x.strftime("%A")) #cara tau hari ini hari apa
# print(x.strftime("%d")) #tanggal
# print(x.strftime("%B")) #bulan
# print(x.strftime("%m")) #bulan dalam angka
# print(x.strftime("%Y")) #tahun full 2020
# print(x.strftime("%y")) #tahun ujungnya 20
# print(x.strftime("%H")) # jam dalam 24 jam
# print(x.strftime("%I")) #jam dalam 12 jam
# print(x.strftime("%p")) # dalam pm / am
# print(x.strftime("%M")) # cari menit
# print(x.strftime("%S")) # detik


# ===================

import datetime
x=datetime.datetime.now()

hari = {
    "Monday":"Senin","Tuesday":"Selasa","Wednesday":"Rabu",
    "Thursday":"Kamis","Friday":"Jumat","Saturday":"Sabtu",
    "Sunday":"Minggu"
}
bulan = {
    "January":"Januari","February":"Februari","March":"Maret",
    "April":"April","May":"Mei","June":"Juni","July":"Juli",
    "August":"Agustus","September":"September","October":"Oktober",
    "November":"November","December":"Desember"
}

class waktu():
    def __init__(self):
        self.hari = hari[x.strftime("%A")]
        self.bulan = bulan[x.strftime("%B")]

waktuku = waktu()


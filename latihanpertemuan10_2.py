# import xlrd #buat baca
# book = xlrd.open_workbook("Book1.xlsx")
# sheet = book.sheet_by_name("halaman1")
# no = []
# nama = []
# usia = []
# kota = []
# for i in range(1,sheet.nrows):
#     no.append(sheet.cell_value(i,0))
#     nama.append(sheet.cell_value(i,1))
#     usia.append(sheet.cell_value(i,2))
#     kota.append(sheet.cell_value(i,3))  

# print(no,nama,kota)
# ==================== read
# data = list(zip(no,nama,usia,kota))
# print(data)
# data = []
# for i in range(1,sheet.nrows):
#     new = []
#     for j in range(sheet.ncols):
#         new.append(sheet.cell_value(i,j))
#     data.append(tuple(new))
# print(data)
    
# print(data)


# print(sheet.nrows)
# print(sheet.ncols)
# print(sheet.cell_value(2,1)) #baris(1,2,3), kolom(a,b,c)

# import xlrd
# book = xlrd.open_workbook("Book1.xlsx")
# sheet = book.sheet_by_name("halaman1")
# for i in range(sheet.nrows):
    # print(sheet.row_values(i))

# ====================================================================
import xlsxwriter
book = xlsxwriter.Workbook("Book1.xlsx")
sheet = book.add_worksheet("halaman1")

data = [
    [1,"andi","jakarta"],
    [2,"budi","jakarta"],
]
row = 0
for no,nama,kota in data:
    sheet.write(row,0,no)
    sheet.write(row,0,nama)
    sheet.write(row,0,kota)
    row += 1

book.close()

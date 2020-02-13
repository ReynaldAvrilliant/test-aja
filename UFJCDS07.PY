# # soal 1
# genap = {2,4,6,8,10,12,14,16,18}
# ganjil = {1,3,5,7,9,11,13,15,17,19}
# negatif = {-10,-9,-8,-7,-6,-5,-4,-3,-2,-1}
# prima = {2,3,5,7,11,13,17,19}
# komposit = {1,4,6,8,9,10,12,14,15,16,18}
# # A ∪ B ∪ C ∪ D ∪ E
# print(genap.union(ganjil,negatif,prima,komposit))
# # (A ∩ B) ∪ (D ∩ E)
# print((genap.intersection(ganjil).union(prima.intersection(komposit))))
# # (A ∪ B) ∩ (D ∪ E)
# print((genap.union(ganjil).intersection(prima.union(komposit))))
# # (A ∪ B) - (D ∪ E)
# print((genap.union(ganjil).difference(prima.union(komposit))))
# # (A ∪ B ∪ C) - (A ∩ E)
# print((genap.union(ganjil,negatif).difference(genap.union(komposit))))


# # nomor 2
# z=""
# kata = "purwadhika coding and startup school @BSD".replace(" ","")
# x = 8
# i = 0
# for row in range (x+1):
#     for col in range(row):
#         z+= kata[i]
#         i+=1
#     z+="\n"
# i = 0
# for row1 in range(x):
#     for col1 in range(x-row1):
#         z+=kata[i]
#         i+=1
#     z+="\n"
# print(z)

# nomor 3

# list
# b = ["banana","orange","apple"]
# print(b)
# temp = b[0]
# b[0] = b[2]
# b[2] = temp
# print(b)
# b[0],b[2] = b[2],b[0]
# print(b)

# # for
# a = ["banana","orange","apple"]
# for i in a:
#     print(i)
# b = [20,10,5]
# total = 0
# for i in b:
#     total = total + i
# print(total)
# ================================

# c = list(range(1,5))
# total= 0
# for i in range(1,5):
#     total += i
# print(total)

# ===============================

# print(list(range(1,8)))
# total3 = 0
# for i in range(1,8):
#     if i % 3 ==0:
#         total3 += i
# print(total3)

# ==================
# total4 = 0
# totalnumber = 0
# for i in range(1,100):
#     if i % 3 ==0 or i % 5 == 0:
#         total4 = total4 + i
#         totalnumber = totalnumber + 1
# print(total4)
# print(totalnumber)

# =======================
# total = 0
# for i in range (1,5):
#     total += i
# print(total)

# while
# total2 = 0
# j = 1
# while j < 5:
#     total2 +=j
#     j+=1
# print(total2)

# 
given_list = [5,4,4,3,1,-2,-3,-5]
total3 = 0
i = 0
while given_list[i]>0:
    total3+=given_list[i]
    i+=1
print(total3)

list_1 = [1,2,3,4,5,6,7,8,9,10,-10,-8,-7,-6,-5,-4,-3,-2,-1]
total4 = 0
i = 0
while list_1[i]>0:
    total4+=list_1[i]
    i+=1
print(total4)
# =========================
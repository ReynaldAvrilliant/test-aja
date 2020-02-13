# nomor 1 


def pangkat(x,y):
    num = 1
    for i in range(y):
        num *= x
    return num
    
print(pangkat(5,2))
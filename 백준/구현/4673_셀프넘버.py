
m = [False]*10000

def kaprekar(num):
    str_num=str(num)
    new_num=num
    for i in range(len(str_num)):
        new_num += int(str_num[i])
    return new_num

for i in range(10000):
    if kaprekar(i)<10000:
        m[kaprekar(i)] = True

for i in range(10000):
    if m[i]==False:
        print(i)

def cycle(num):

    if num<10:
        num = int('0'+str(num))
        return 10*(num%10)+((num//10 + num%10)%10)
    else:
        return 10*(num%10)+((num//10 + num%10)%10)

n = int(input())

new_num = n
count = 0

while True:
    new_num=cycle(new_num)
    count += 1
    if new_num==n:
        break

print(count)
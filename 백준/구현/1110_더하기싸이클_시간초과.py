def GenerateNewNum(num):
    if len(num) == 1:
        num = '0' + num
    new_num = int(num[0]) + int(num[1])
    new_num = num[1] + str(new_num % 10)
    return new_num

num = input().strip()
original_num = num
count = 0

while True:
    count += 1
    new_num = GenerateNewNum(num)
    if new_num == original_num:
        break
    num = new_num
print(count)
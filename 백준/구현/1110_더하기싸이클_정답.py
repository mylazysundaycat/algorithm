def generate_new_num(num):
    # num을 두 자리로 맞추기 위해 필요한 경우 앞에 0을 붙임
    a = num // 10
    b = num % 10
    new_num = (b * 10) + ((a + b) % 10)
    return new_num

num = int(input().strip())
original_num = num
count = 0

while True:
    count += 1
    num = generate_new_num(num)
    if num == original_num:
        break

print(count)
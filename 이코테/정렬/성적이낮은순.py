
num = int(input())

arr = []

for i in range(num):
    input_data = input().split()
    arr.append((input_data[0], int(input_data[1])))

arr.sort(key=lambda x:x[1])

for i in arr:
    print(i[0], end=' ')



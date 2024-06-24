arr = list()

for i in range(9):
    arr.append(int(input()))

max = arr[0]
index = 0

for i in range(1,9):
    if max<arr[i]:
        max = arr[i]
        index = i

print(max)
print(index+1)
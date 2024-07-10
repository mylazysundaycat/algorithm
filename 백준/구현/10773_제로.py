
n = int(input())

arr = []

for _ in range(n):
    x = int(input())
    if x == 0:
        arr.pop()
        continue
    arr.append(x)

print(sum(arr) if arr else 0)
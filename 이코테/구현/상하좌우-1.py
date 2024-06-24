n = int(input())

route = input().split()
length = len(route)

# 여행가A 초기화
user = [1, 1]

for i in range(length):
    if route[i] == 'R':
        if user[1] < n:
            user[1] += 1
    if route[i] == 'U':
        if user[0] > 1:
            user[0] -= 1
    if route[i] == 'D':
        if user[0] < n:
            user[0] += 1
    if route[i] == 'L':
        if user[1] > 1:
            user[1] -= 1

print(user[0],user[1])

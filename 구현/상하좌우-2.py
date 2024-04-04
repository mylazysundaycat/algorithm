n = int(input())
x, y = 1, 1
route = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for r in route:
    for i in range(len(move_types)):
        if r == move_types[i]:
            rx = x + dx[i]
            ry = y + dy[i]
    if rx < 1 or ry < 1 or rx > n or ry > n:
        continue
    x, y = rx, ry

print(x, y)

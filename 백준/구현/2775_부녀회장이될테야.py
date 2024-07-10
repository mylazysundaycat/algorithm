
lst = [[0]*14 for _ in range(15)]

for i in range(0,14):
    lst[0][i] = i+1

for i in range(1,15):
    for j in range(14):
        lst[i][j] = sum(lst[i-1][:j+1])

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(lst[k][n-1])
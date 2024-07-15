import sys

input = sys.stdin.readline

t = int(input())


for _ in range(t):
    n = int(input())
    lst = list()
    for i in range(n):
        lst.append(list(map(int, input().split(' '))))
    lst.sort(key=lambda x:x[0])

    cnt=1
    check = lst[i][1]
    for i in range(1,n):
        if check>lst[i][1]:
            cnt += 1
            check=lst[i][1]

    print(cnt)
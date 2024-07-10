n = int(input())
e = []

for k in range(n//3 + 1):
    for m in range(n//5 + 1):
        if 3*k + 5*m <= n:
            if 3*k + 5*m == n:
                f = k+m
                e.append(f)
if len(e) == 0:
    print(-1)
else:
    print(min(e))
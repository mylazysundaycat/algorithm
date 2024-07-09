n = int(input())

blank=' '
star='*'

for i in range(n,0,-1):
    print(blank*(n-i)+star*i)


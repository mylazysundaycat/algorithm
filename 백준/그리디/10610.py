import sys

x=sys.stdin.readline().rstrip()
x=sorted(x,reverse=True)
sum=0
if '0' not in x:
    print(-1)
else:
    for i in x:
        sum += int(i)
    if sum%3!=0:
        print(-1)
    else:
        print(''.join(x))


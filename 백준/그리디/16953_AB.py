import sys

k, n = map(int, sys.stdin.readline().split(' '))

count = 0
while True:
    if n==k:
        break
    elif (n%2!=0 and n%10!=1) or n<k:
        print(-1)
        sys.exit(0)
    elif n%2==0:
        n=n//2
        count+=1
    elif n%10==1:
        n=n//10
        count+=1

print(count+1)


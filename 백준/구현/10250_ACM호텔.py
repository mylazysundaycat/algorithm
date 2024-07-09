import sys

t = int(input().rstrip())


for _ in range(t):
    h,w,n = map(int,sys.stdin.readline().split(' '))
    print((n%h)*100 + ((n//h)+1))



t = int(input())

for _ in range(t):
    h,w,n = map(int,input().split(' '))
    if n%h==0:
        print(h*100 + n//h                  )
    else:
        print((n%h)*100 + ((n//h)+1))
n,k = map(int,input().split(' '))

lst=[0]*n

for i in range(n):
    lst[i]=int(input())

lst.sort(reverse=True)

count = 0

i=0
while k>0:
    if k//lst[i]>0:
        count+=k//lst[i]
        k=k%lst[i]
    i+=1

print(count)

n=int(input())
count=0
i=0
while True:
    i+=1
    n -= i
    if i>=n:
        break
    count += 1

print(count+1)
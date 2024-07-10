
N=int(input())
count =0

if N//5>0:
    for i in range(N//5):
        count += N//5-i
        new_N=N-((N//5-i)*5)
        if new_N%3==0:
            count += new_N//3
            break
        else:
            count = 0
    if count==0:
        if N%3==0:
            count+=N//3
        else:
            count=-1
else:
    if N%3==0:
        count+=N//3
    else:
        count=-1
print(count)

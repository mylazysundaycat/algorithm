import sys
x=sys.stdin.readline().rstrip()


# one=x.split('0')
# zero=x.split('1')
# print(one)
# print(zero)
#
# if len(one[0])==len(x) or len(one[1])==len(x):
#     print(0)
# else:
#     print(min(len(one), len(zero)))


prev=x[0]
a=''+x[0]
lst=[]
for i in range(1,len(x)):
    if prev==x[i]:
        a+=x[i]
    else:
        lst.append(a)
        a=''+x[i]
        prev=x[i]
    if i==len(x)-1:
        lst.append(a)

zero=0
one=0
for i in range(len(lst)):
    if lst[i].startswith('0'):
        zero+=1
    elif lst[i].startswith('1'):
        one+=1

print(0 if zero==0 or one==0 else min(zero,one))

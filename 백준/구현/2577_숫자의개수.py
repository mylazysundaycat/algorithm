a = int(input())
b = int(input())
c = int(input())
d = str(a*b*c)

num_dict = dict()

for i in range(len(d)):
    if d[i] not in num_dict:
        num_dict[d[i]] = 1
    else:
        num_dict[d[i]] += 1

for num in range(10):
    if str(num) in num_dict:
        print(num_dict[str(num)])
    else:
        print(0)

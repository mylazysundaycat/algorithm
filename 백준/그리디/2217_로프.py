n = int(input())
lst = []
for i in range(n):
    lst.append(int(input()))
lst.sort()
weight_lst = []
for i in range(n):
    weight_lst.append((n-i)*lst[i])
print(max(weight_lst))
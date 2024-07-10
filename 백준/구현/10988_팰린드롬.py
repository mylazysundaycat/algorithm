x = input()
result = 1
for i in range(len(x)//2):
    if x[i]==x[len(x)-1-i]:
        continue
    else:
        result = 0
        break

print(result)
pivo = [0,1]

for i in range(2,21):
    pivo.append(pivo[i-1]+pivo[i-2])


n = int(input())

print(pivo[n])
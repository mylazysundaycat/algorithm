
arr = list(map(ord, input()))

print(arr)

alphabet = [0]*26

for i in range(len(arr)):
    if arr[i]>96:
        alphabet[arr[i]-97] += 1
    else:
        alphabet[arr[i]-65] +=1

print(alphabet)

max = -1
index = 0
result = ""
for i in range(len(alphabet)):
    if max<alphabet[i]:
        max = alphabet[i]
        index = i
    elif max==alphabet[i]:
        result = "?"

if result == "?":
    print(result)
else:
    print(chr(index+65))
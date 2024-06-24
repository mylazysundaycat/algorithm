alphabet_arr = [-1]*26

str_input = input().strip()

for i in range(len(str_input)):
    if alphabet_arr[ord(str_input[i])-97] != -1:
        continue
    alphabet_arr[ord(str_input[i])-97] = i

for i in range(26):
    print(alphabet_arr[i],end=' ')
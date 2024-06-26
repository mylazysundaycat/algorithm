# 입력 받기
word = input().strip().lower()

# 알파벳 빈도 수 계산
alphabet = [0] * 26

for char in word:
    alphabet[ord(char) - ord('a')] += 1

# 최댓값 찾기
max_count = max(alphabet)
if alphabet.count(max_count) > 1:
    print('?')
else:
    print(chr(alphabet.index(max_count) + ord('A')))
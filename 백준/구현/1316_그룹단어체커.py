

def isGroupWord(word):
    group = set()
    prev_word = ''
    for w in word:
        if prev_word!=w:
            if w in group:
                return False
            group.add(w)
        prev_word = w
    return True

n = int(input().strip())
group_word_count = 0

for _ in range(n):
    word = input().strip()
    if isGroupWord(word):
        group_word_count += 1

print(group_word_count)
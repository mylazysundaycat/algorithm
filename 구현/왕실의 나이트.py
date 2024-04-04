location = input()

row = int(location[1])
col = int(ord(location[0]) - ord('a')) + 1

move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

count = 0

for m in range(len(move)):
    tRow = row + move[m][0]
    tCol = col + move[m][1]
    if tRow < 1 or tCol < 1 or tRow > 8 or tCol > 8:
        continue
    count += 1
print(count)

N = int(input())

line = 0
line_end_num = 0

while line_end_num < N:
    line += 1
    line_end_num += line

K = line_end_num - N

if line % 2 == 0:
    a = line - K
    b = K + 1
else:
    a = K + 1
    b = line - K

print(str(a) + '/' + str(b))
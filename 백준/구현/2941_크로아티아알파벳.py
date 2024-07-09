# import sys
#
# s = sys.stdin.readline().strip()
#
# count = 0
# i = 0
#
# while i < len(s):
#     if s[i:i+3] == 'dz=':
#         i += 3
#     elif s[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
#         i += 2
#     else:
#         i += 1
#     count += 1
#
# print(count)


import sys

s = sys.stdin.readline().rstrip()

count = 0
while s:
    if s.startswith('c='):
        s = s[2:]
        count += 1
    elif s.startswith('c-'):
        s = s[2:]
        count += 1
    elif s.startswith('d-'):
        s = s[2:]
        count += 1
    elif s.startswith('lj'):
        s = s[2:]
        count += 1
    elif s.startswith('nj'):
        s = s[2:]
        count += 1
    elif s.startswith('s='):
        s = s[2:]
        count += 1
    elif s.startswith('z='):
        s = s[2:]
        count += 1
    elif s.startswith('dz='):
        s = s[3:]
        count += 1
    else:
        s = s[1:]
        count += 1

print(count)
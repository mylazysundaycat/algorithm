
star = '*'
blank = ' '

n = int(input())
num = (2*n)-1
num_half = num//2
for i in range(num):
    if i<=num_half:
        print(blank*(num_half-i)+star*(2*i+1))
    else:
        print(blank*(i-num_half)+star*(num-2*(i-num_half)))


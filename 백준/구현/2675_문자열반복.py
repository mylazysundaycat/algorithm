n = int(input())

def str_circle(input_str,num):
    new_str = ''
    for i in range(len(input_str)):
        new_str += input_str[i]*num
    return new_str

for i in range(n):
    num, input_str = input().split()
    print(str_circle(input_str,int(num)))
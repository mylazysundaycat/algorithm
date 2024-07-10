n=int(input())
lst=list()

for _ in range(n):
    x, y = map(int, input().split(' '))
    lst.append([x,y])

for i in range(n):
    count = 0
    for j in range(n):
        x_bool = False
        y_bool = False
        if lst[i][0]< lst[j][0]:
            x_bool = True
        if lst[i][1]< lst[j][1]:
            y_bool = True
        if x_bool and y_bool == True:
            count += 1
    print(count+1)


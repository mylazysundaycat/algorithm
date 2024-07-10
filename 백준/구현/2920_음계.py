
ascending=[1,2,3,4,5,6,7,8]

descending=[8,7,6,5,4,3,2,1]

keybord = list(map(int,input().split(' ')))

if keybord==ascending:
    print('ascending')
elif keybord==descending:
    print('descending')
else:
    print('mixed')
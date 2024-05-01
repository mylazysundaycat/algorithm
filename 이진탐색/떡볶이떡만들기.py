n, m = map(int, input().split())

arr = list(map(int,input().split()))

def cut(arr, cut):
    notZero = 0
    for i in range(len(arr)):
        if arr[i]>=cut:
            arr[i] = arr[i]-cut
            notZero += 1
        else:
            arr[i] = 0

    x = sum(arr)//notZero
    return x+cut


max = cut(arr, m)
print(max)


def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2

    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    elif array[mid]<target:
        return binary_search(array,target,mid+1,end)


n = int(input())
nArr = list(map(int, input().split()))
nArr.sort()

m = int(input())
mArr = list(map(int,input().split()))

for i in range(m):
    result = binary_search(nArr, mArr[i], 0, len(nArr)-1)
    if result:
        print("yes", end=' ')
    else:
        print("no", end=' ')

array = [5,7,8,0,3,1,6,2,4,8]
def quick_sort(array, start, end):
    if start>=end: #원소가 1개인 경우 종료
        return

    pivot = start #피벗은 첫 번째 원소
    left = start+1
    right = end

    while left<=right:
        #왼쪽부터 피벗보다 큰 데이터를 찾을때까지 반복
        while left<=end and array[left]<=array[pivot]:
            left += 1

        #오른쪽부터 피벗보다 작은 데이터를 찾을 때 까지 반복
        while right>start and array[right]>array[pivot]:
            right -= 1

        #left와 right가 엇갈렸다면
        #while문이 이후 종료됨
        if left>right:
            array[right], array[pivot] = array[pivot], array[right],
        #left와 right가 엇갈리지 않았다면
        else:
            array[left], array[right] = array[right], array[left]

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 수행
    quick_sort(array,start, right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)
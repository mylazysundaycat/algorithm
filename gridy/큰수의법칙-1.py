
n, m, k = map(int, input().split())
#리스트 받아오기
data = list(map(int, input().split()))
#데이터 정렬
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m==0: break
        result += first
        m -= 1
    if m==0: break
    result += second
    m -= 1

print(result)


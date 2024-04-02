n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

#큰 수를 곱하는 몫을 미리 구한다면,
#iterable을 사용하지 않아도 답을 구할 수 있다.
count = int(m/(k+1))*k
count += m%(k+1)

result = first*count + second*(m-count)

print(result)
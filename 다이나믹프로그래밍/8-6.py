from sys import stdin

#dp 테이블은 i번째 식량창고까지 털었을때의 최댓값이다.
dp = [0]*101

n = int(input())
arr = list(map(int, stdin.readline().split()))


dp[0] = arr[0]
dp[1] = max(arr[0],arr[1])

for i in range(2,n):
    dp[i] = max(dp[i-1], dp[i-2]+arr[i])

print(dp[n-1])

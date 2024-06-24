import sys
input = sys.stdin.readline()

x = int(input())


#최소연산수를 가질 테이블
dp = [0]*30001

for i in range(2,x):

    dp[i] = dp[i-1]+1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)

print(dp[x])
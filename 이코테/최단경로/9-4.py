
INF = int(1e9)

# n: 회사의 갯수
# m: 경로의 갯수
n,m = map(int, input().split())
graph = [[INF]*(n+1) for i in range(n+1)]

for i in range(1, m+1):
    for j in range(1, m+1):
        if i==j:
            graph[i][j] = 0

for i in range(1, m+1):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print("-1")
else:
    print(distance)
    

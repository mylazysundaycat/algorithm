from collections import deque

n, m = map(int, input().split())

# 맵 정보 2차원리스트
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 아래 위 오른쪽 왼쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    while queue:
        # 큐에서 원소를 하나 출력
        x,y = queue.popleft()
        # 원소와 연결된 노드를 큐에 입력
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0,0))

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
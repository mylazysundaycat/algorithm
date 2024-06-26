n, m = map(int, input().split())

#맵 정보
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

#모든 노드 방문
def dfs(x,y):
    if x<=-1 or y<=-1 or x>=n or y>=m:
        return False
    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            count+=1

print(count)

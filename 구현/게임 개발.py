row, col = map(int, input().split())
x, y, direction = map(int, input().split())


#맵 2차원 배열 생성
gameMap = []
for i in range(row):
    gameMap.append(list(map(int, input().split())))

#맵 방문 여부 저장
#0이면 미방문 1이면 방문
booleanMap = [[0]*col for _ in range(row)]

#방향 북,동,남,서
s_direction = [0,1,2,3]

#변위 북,동,남,서
dx = [1,0,-1,0]
dy = [0,1,0,-1]

#왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3



count = 0
turn_count = 0
while True:
    turn_left()
    n_x = x+dx[direction]
    n_y = y+dy[direction]

    #방문한적 없는 경우
    if booleanMap[n_x][n_y]==0 and gameMap[n_x][n_y]==0:
        x = n_x
        y = n_y
        count += 1
        booleanMap[n_x][n_y]=1 #방문표시
        turn_time = 0
        continue
    else: #바다인 경우
        turn_count+=1 #회전횟수 추가

    #네 방향 모두 가본적이 있는 경우
    if turn_count == 4:
        n_x = x - dx[direction]
        n_y = y - dx[direction]

        #뒤쪽이 육지인 경우
        if gameMap[n_x][n_y] == 0:
            x = n_x #뒤로 간다
            y = n_y
        #뒤쪽이 바다인 경우
        else:
            break
        turn_count = 0

print(count)





# for gm in gameMap:
#     for g in gm:
#         print(g,end=" ")

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
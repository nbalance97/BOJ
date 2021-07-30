import sys
from collections import deque

input = sys.stdin.readline

# 불 확산 함수


Fire = deque()
def spread(matrix, R, C):
    global Fire
    stop_flag = 0
    if Fire:
        stop_flag = Fire[0][2]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while Fire:
        if Fire[0][2] > stop_flag:
            break
        cx, cy, step = Fire.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx and nx < R and 0 <= ny and ny < C:
                if matrix[nx][ny] == '.' or matrix[nx][ny] == 'J':
                    matrix[nx][ny] = 'F'
                    Fire.append([nx, ny, step+1])


R, C = map(int, input().rstrip().split())
matrix = [list(input().rstrip()) for _ in range(R)]

for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'F':
            Fire.append([i, j, 0])

J_x, J_y = 0, 0
flag = False
# 지훈이의 위치 찾음
for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'J':
            J_x, J_y = i, j
            flag = True
            break
    if flag:
        break


Jh_queue = deque([[J_x, J_y, 0]])
visited = set()
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
last = 0
visited.add((J_x, J_y))
answer_flag = False
answer = 0
while Jh_queue:
    jx, jy, movement_count = Jh_queue.popleft()
    # 이동 횟수가 늘어나면 불 확
    if last != movement_count:
        spread(matrix, R, C)
        last = movement_count

    # 현재 방문하려는 위치에 이미 불 퍼진 상태면 스킵
    if matrix[jx][jy] == 'F':
        continue
    
    for i in range(4):
        nx, ny = jx + dx[i], jy + dy[i]
        if 0 <= nx and nx < R and 0 <= ny and ny < C:
            if matrix[nx][ny] == '.' and (nx, ny) not in visited:
                Jh_queue.append([nx, ny, movement_count+1])
                visited.add((nx, ny))
        elif 0 > nx or nx >= R or 0 > ny or ny >= C:
            answer_flag = True
            answer = movement_count + 1
            break
    if answer_flag:
        break

if answer_flag:
    print(answer)
else:
    print("IMPOSSIBLE")
    
            
                

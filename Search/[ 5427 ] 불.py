import sys
from collections import deque
import copy

input = sys.stdin.readline

T = int(input().rstrip())

def expand(matrix, fire):
    temp = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    w, h = len(matrix[0]), len(matrix)
    for x, y in fire:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < h and 0 <= ny and ny < w:
                if matrix[nx][ny] == '.':
                    matrix[nx][ny] = '*'
                    temp.append([nx, ny])
                    
    return temp

for _ in range(T):

    # 입력부
    w, h = map(int, input().rstrip().split())
    matrix = [list(input().rstrip()) for _ in range(h)]
    # 초기
    visited = [[False] * w for _ in range(h)] 
    person_x, person_y = 0, 0
    fire = []
    # 불, 사람의 위치 저장
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == '@':
                person_x, person_y = i, j
            if matrix[i][j] == '*':
                fire.append([i, j])
                
    queue = deque([[person_x, person_y, 0]])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited[person_x][person_y] = True
    before = 0
    end = False
    while queue:
        x, y, step = queue.popleft()
        # 이동 => 불 확산
        if before != step:
            # 불 확산 + 확산된 불의 위치 저장
            fire = expand(matrix, fire)
            before = step
            
        if matrix[x][y] == '*':
            # 이번에 갈 곳에 불이 이미 번졌으면 못감
            continue
        
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx and nx < h and 0 <= ny and ny < w:
                if not visited[nx][ny] and matrix[nx][ny] == '.':
                    visited[nx][ny] = True
                    queue.append([nx, ny, step+1])
            else:
                # 범위 벗어나면 탈출한것이므로 출력
                print(step+1)
                end = True
                break
        if end:
            break
    if not end:
        print("IMPOSSIBLE")
        

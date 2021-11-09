import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]

water_pos = deque()
visited_biber = set()
biber = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(R):
    for j in range(C):
        if matrix[i][j] == '*':
            water_pos.append([i, j])
        if matrix[i][j] == 'S':
            visited_biber.add((i, j))
            biber.append([i, j, 0])
            
def flood():
    global R, C, water_pos
    next_deque = deque()
    while water_pos:
        x, y = water_pos.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < R and 0 <= ny and ny < C and \
               matrix[nx][ny] not in ['X', 'D', '*']:
                next_deque.append([nx, ny])
                matrix[nx][ny] = '*'
    water_pos = next_deque

step = -1
while biber:
    x, y, current_step = biber.popleft()
    if matrix[x][y] == '*':
        continue
    if matrix[x][y] == 'D':
        print(current_step)
        break
    
    if current_step != step:
        step = current_step
        flood()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx and nx < R and 0 <= ny and ny < C:
            if matrix[nx][ny] != '*' and matrix[nx][ny] != 'X' and \
               (nx, ny) not in visited_biber:
                visited_biber.add((nx, ny))
                biber.append([nx, ny, current_step+1])
else:
    print('KAKTUS')

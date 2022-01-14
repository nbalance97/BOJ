import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def get_air_pos():
    air = set()
    air.add((0, 0))
    queue = deque([[0, 0]])
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < N and 0 <= ny and ny < M:
                if (nx, ny) not in air and matrix[nx][ny] == 0:
                    air.add((nx, ny))
                    queue.append([nx, ny])

    return air

def is_empty():
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                return False
    return True

def destroy_cheese(air):
    destroy_cheese_pos = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                air_count = 0
                for k in range(4):
                    x, y = i + dx[k], j + dy[k]
                    if (x, y) in air:
                        air_count += 1
                if air_count >= 2:
                    destroy_cheese_pos.append([i, j])
                    
    for x, y in destroy_cheese_pos:
        matrix[x][y] = 0
                            

time = 0
while True:
    if is_empty():
        break
    air = get_air_pos()
    destroy_cheese(air)
    time += 1
    

print(time)

    

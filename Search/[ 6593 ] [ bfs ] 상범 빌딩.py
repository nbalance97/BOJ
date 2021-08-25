import sys
import copy
from collections import deque

input = sys.stdin.readline

def input_matrix(matrix, R):
    floor = [list(input().rstrip()) for _ in range(R)]
    matrix.append(floor)

def get_start_point(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(len(matrix[0][0])):
                if matrix[i][j][k] == 'S':
                    return [i, j, k, 0]

while True:
    L, R, C = map(int, input().rstrip().split())
    if L == 0 and R == 0 and C == 0:
        break
    
    matrix = []
    for _ in range(L):
        input_matrix(matrix, R)
        input() # 1칸 띄워줌
        
    start = get_start_point(matrix)
    visited = copy.deepcopy(matrix)
    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    queue = deque([start])
    answer = -1
    while queue:
        x, y, z, cost = queue.popleft()
        if matrix[x][y][z] == 'E':
            answer = cost
            break
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx and nx < L and 0 <= ny and ny < R and 0 <= nz and nz < C:
                if not visited[nx][ny][nz] == 'O' and matrix[nx][ny][nz] != '#':
                    queue.append([nx, ny, nz, cost+1])
                    visited[nx][ny][nz] = 'O'

    if answer != -1:
        print("Escaped in %d minute(s)."%(answer))
    else:
        print("Trapped!")

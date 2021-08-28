import sys
import copy
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]


def minus(temp, matrix, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < len(matrix) and 0 <= ny and ny < len(matrix[0]):
            if matrix[nx][ny] == 0:
                temp[x][y] -= 1

    if temp[x][y] < 0:
        temp[x][y] = 0

def bfs(matrix, x, y):
    queue = deque([[x, y]])
    matrix[x][y] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < len(matrix) and 0 <= ny and ny < len(matrix[0]):
                if matrix[nx][ny] != 0:
                    matrix[nx][ny] = 0
                    queue.append([nx, ny])
year = 1
while True:
    # 빙산 녹는 과정 시뮬레이션
    temp = copy.deepcopy(matrix)
    for i in range(N):
        for j in range(M):
            if matrix[i][j] != 0:
                minus(temp, matrix, i, j)
                
    # matrix에 녹은 빙산 저장 
    matrix = copy.deepcopy(temp)

    # 녹은 빙산이 몇덩이인지 bfs로 검사
    total = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] != 0:
                total += 1
                bfs(temp, i, j)

    # 덩어리의 수에 따라 출력
    if total >= 2:
        print(year)
        break
    elif total == 0:
        print(0)
        break
    
    year += 1

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
matrix = [list(input()) for _ in range(m)]

def bfs(matrix, x, y):
    target = matrix[x][y]
    count = 1
    matrix[x][y] = "."
    queue = deque()
    row = len(matrix)
    col = len(matrix[0])
    
    queue.append([x, y])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if matrix[nx][ny] == target:
                    queue.append([nx, ny])
                    matrix[nx][ny] = '.'
                    count += 1

    return count

W_c, B_c = 0, 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] != '.':
            if matrix[i][j] == "W":
                W_c += bfs(matrix, i, j) ** 2
            elif matrix[i][j] == "B":
                B_c += bfs(matrix, i, j) ** 2

print(W_c, B_c)
            
    
    

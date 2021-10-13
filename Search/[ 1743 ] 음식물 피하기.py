import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())

matrix = [[0] * (M+1) for _ in range(N+1)]

def bfs(matrix, x, y):
    count = 1
    matrix[x][y] = 0
    queue = deque([[x, y]])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and \
               matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                count += 1
                queue.append([nx, ny])

    return count

for _ in range(K):
    a, b = map(int, input().split())
    matrix[a][b] = 1

answer = 0
for i in range(1, N+1):
    for j in range(1, M+1):
        if matrix[i][j] == 1:
            answer = max(answer, bfs(matrix, i, j))

print(answer)
        
    

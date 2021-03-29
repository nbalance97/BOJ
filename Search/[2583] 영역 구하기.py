import sys
from collections import deque

input = sys.stdin.readline
M, N, K = map(int, input().rstrip().split())

matrix = [[0] * N for _ in range(M)]

def bfs(i, j):
    global N, M
    queue = deque()
    queue.append([i, j])
    matrix[i][j] = 1
    count = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < M and ny >= 0 and ny < N: 
                if matrix[nx][ny] == 0:
                    queue.append([nx, ny])
                    matrix[nx][ny] = 1
                    count += 1

    return count

for _ in range(K):
    y1, x1, y2, x2 = map(int, input().rstrip().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            matrix[i][j] = 1
            
answer = []
for i in range(M):
    for j in range(N):
        if matrix[i][j] == 0:
            answer.append(bfs(i, j))

print(len(answer))
answer.sort()
print(" ".join(map(str, answer)))

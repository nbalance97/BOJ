import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
total_visited = [[False] * M for _ in range(N)]


def bfs(matrix, x, y):
    queue = deque()
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]

    visited = [[False] * M for _ in range(N)]
    queue.append([x, y, matrix[x][y]])
    visited[x][y] = True
    total_visited[x][y] = True

    check = True
    while queue:
        cx, cy, ch = queue.popleft()
        for i in range(8):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and not visited[nx][ny]:
                if matrix[nx][ny] > ch:
                    check = False
                elif matrix[nx][ny] == ch:
                    queue.append([nx, ny, ch])
                    visited[nx][ny] = True
                    total_visited[nx][ny] = True
                else:
                    visited[nx][ny] = True

    return check

answer = 0
for i in range(N):
    for j in range(M):
        if not total_visited[i][j]:
            if bfs(matrix, i, j):
                answer += 1

print(answer)

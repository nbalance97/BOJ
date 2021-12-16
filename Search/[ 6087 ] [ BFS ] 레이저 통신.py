import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
W, H = map(int, input().split())
matrix = [list(input()) for _ in range(H)]

C = [(i, j) for i in range(H) for j in range(W) if matrix[i][j] == 'C']

def bfs(matrix, start, end):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    startX, startY = start
    endX, endY = end
    visited = [[[int(10e9)] * 4 for i in range(W)] for j in range(H)]
    visited[startX][startY] = [0, 0, 0, 0]
    queue = deque()
    
    for i in range(4):
        nx, ny = startX + dx[i], startY + dy[i]
        if 0 <= nx and nx < H and 0 <= ny and ny < W:
            if matrix[nx][ny] != '*':
                visited[nx][ny][i] = 0
                queue.append([nx, ny, i])

    while queue:
        x, y, d = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < H and 0 <= ny and ny < W:
                if matrix[nx][ny] != '*':
                    if i == d:
                        if visited[nx][ny][i] > visited[x][y][d]:
                            visited[nx][ny][i] = visited[x][y][d]
                            queue.appendleft([nx, ny, i])
                    else:
                        if visited[nx][ny][i] > visited[x][y][d] + 1:
                            visited[nx][ny][i] = visited[x][y][d] + 1
                            queue.append([nx, ny, i])

    return min(filter(lambda x:x>=0, visited[endX][endY]))



print(bfs(matrix, C[0], C[1]))
    

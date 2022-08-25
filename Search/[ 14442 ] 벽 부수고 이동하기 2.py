import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
matrix = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()

queue.append([0, 0, 1, 0])
visited = [[[False] * (k+1) for _ in range(m)] for __ in range(n)]
visited[0][0][0] = True

answer = -1
while queue:
    x, y, movement_count, destroy_count = queue.popleft()
    if x == n-1 and y == m-1:
        answer = movement_count
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 0 and not visited[nx][ny][destroy_count]:
                queue.append([nx, ny, movement_count + 1, destroy_count])
                visited[nx][ny][destroy_count] = True
            if matrix[nx][ny] == 1 and destroy_count < k and not visited[nx][ny][destroy_count+1]:
                queue.append([nx, ny, movement_count + 1, destroy_count + 1])
                visited[nx][ny][destroy_count+1] = True

print(answer)

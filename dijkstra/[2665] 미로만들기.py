import sys
import copy
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())

# bfs와 유사하나 원리 자체가 dijkstra와 유사함.

INT_MAX = sys.maxsize

matrix = []
for _ in range(n):
    matrix.append(list(map(int, list(input().rstrip()))))

visited_BLACK = [[INT_MAX] * n for _ in range(n)] # 검은 칸 방문 횟수 저장

queue = deque()
queue.append([0, 0, 0])
visited_BLACK[0][0] = 0 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, b = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 현재 칸 거쳐서 갈때가 검은 칸 방문 횟수 더 적은 경우 갱신 및 큐 삽입
            if matrix[nx][ny] == 0 and visited_BLACK[nx][ny] > b+1:
                visited_BLACK[nx][ny] = b+1
                queue.append([nx, ny, b+1])
            elif matrix[nx][ny] == 1 and visited_BLACK[nx][ny] > b:
                visited_BLACK[nx][ny] = b
                queue.append([nx, ny, b])

print(visited_BLACK[n-1][n-1])
    

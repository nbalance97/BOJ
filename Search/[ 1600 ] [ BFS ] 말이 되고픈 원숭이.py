import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

K = int(input())
W, H = map(int, input().split())
visited = [set() for _ in range(K+1)]
answer = 0

matrix = [list(map(int, input().split())) for _ in range(H)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
horse_dx = [-2, -2, -1, -1, 1, 1, 2, 2]
horse_dy = [-1, 1, -2, 2, -2, 2, 1, -1]

queue = deque([[0, 0, 0, 0]])
visited[0].add((0, 0))
answer = int(10e9)

def check_and_visit(x, y, m, h_m):
    global W, H
    if 0 <= x and x < H and 0 <= y and y < W:
        if (x, y) not in visited[h_m] and matrix[nx][ny] != 1:
            visited[h_m].add((x, y))
            queue.append([x, y, h_m, m])

while queue:
    x, y, h_m, m = queue.popleft()

    if x == H-1 and y == W-1:
        answer = m
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        check_and_visit(nx, ny, m+1, h_m)

    if h_m < K:
        for i in range(8):
            nx, ny = x + horse_dx[i], y + horse_dy[i]
            check_and_visit(nx, ny, m+1, h_m+1)


if answer == int(10e9):
    print(-1)
else:
    print(answer)

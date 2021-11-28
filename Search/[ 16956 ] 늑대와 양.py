import sys
from collections import deque

# 비어있는 칸들을 모두 울타리로 칠해버린 다음, 늑대가 양 위치에 도달 가능한지만 조사

input = lambda: sys.stdin.readline().rstrip()
r, c = map(int, input().split())
matrix = [list(input()) for _ in range(r)]
wolf = deque()
for i in range(r):
    for j in range(c):
        if matrix[i][j] == '.':
            matrix[i][j] = 'D'
        if matrix[i][j] == 'W':
            wolf.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
can = True
while wolf:
    x, y = wolf.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx and nx < r and 0 <= ny and ny < c:
            if matrix[nx][ny] == 'S':
                can = False
                break

    if not can:
        break

if not can:
    print(0)
else:
    print(1)
    for m in matrix:
        print("".join(m))

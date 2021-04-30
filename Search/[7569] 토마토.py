import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().rstrip().split())

matrix = []
# [높이][행][열]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
count = 0

for i in range(h):
    short = []
    for j in range(n):
        short.append(list(map(int, input().rstrip().split())))
    matrix.append(short)

candidate = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1:
                candidate.append([i, j, k, 0]) # 토마토의 위치 + 현재 몇번째 bfs인지까지 queue에 삽입

def bfs():
    global count
    global m, n, h
    while candidate:
        if candidate[0][3] != count:
            count = count + 1
            return
        x, y, z, c = candidate.popleft()
        for i in range(6):
            next_x = x + dx[i]
            next_y = y + dy[i]
            next_z = z + dz[i]
            if 0 <= next_x and next_x < h and 0 <= next_y and next_y < n and 0 <= next_z and next_z < m:
                if matrix[next_x][next_y][next_z] == 0:
                    matrix[next_x][next_y][next_z] = 1
                    candidate.append([next_x, next_y, next_z, c+1])

while candidate: # 후보군이 모두 없어질때까지 bfs 돌림
    bfs()

succeed = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                succeed = False
                break
        if not succeed:
            break
    if not succeed:
        break

if not succeed:
    print(-1)
else:
    print(count)

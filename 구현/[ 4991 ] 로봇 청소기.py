import sys
from collections import deque
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()
WALL, FURNITURE, ROBOT = 'x', '*', 'o'

def bfs(room, idx_mapper, dist, orgx, orgy):
    visited = [[False] * len(room[0]) for _ in range(len(room))]
    visited[orgx][orgy] = True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[orgx, orgy, 0]])
    current_idx = idx_mapper[(orgx, orgy)]
    while queue:
        x, y, movement_count = queue.popleft()
        if room[x][y] == '*':
            dist[current_idx][idx_mapper[(x,y)]] = movement_count
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < len(room) and 0 <= ny and ny < len(room[0]):
                if not visited[nx][ny] and room[nx][ny] != WALL:
                    visited[nx][ny] = True
                    queue.append([nx, ny, movement_count+1])

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break
    room = [list(input()) for _ in range(M)]
    furniture_count = 1
    idx_mapper = {}
    idx_mapper_reverse = {}

    for i in range(M):
        for j in range(N):
            if room[i][j] == 'o':
                room[i][j] = '*'
                idx_mapper[(i, j)] = 0
                idx_mapper_reverse[0] = (i, j)  
            elif room[i][j] == '*':
                idx_mapper[(i, j)] = furniture_count
                idx_mapper_reverse[furniture_count] = (i, j)
                furniture_count += 1

    dist = [[-1] * furniture_count for _ in range(furniture_count)]

    for i in range(furniture_count):
        x, y = idx_mapper_reverse[i]
        bfs(room, idx_mapper, dist, x, y)
        
    answer = int(10**9)
    for seq in list(permutations([i for i in range(1, furniture_count)])):
        temp = dist[0][seq[0]]
        if temp == -1:
            continue
        end = False
        for i in range(1, len(seq)):
            if dist[seq[i]][seq[i-1]] == -1:
                end = True
                break
            else:
                temp += dist[seq[i]][seq[i-1]]
        if end:
            continue
        answer = min(answer, temp)

    if answer == int(10**9):
        print(-1)
    else:
        print(answer)

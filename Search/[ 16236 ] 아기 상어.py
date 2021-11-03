import sys
from collections import deque


input = lambda: sys.stdin.readline().rstrip()

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

# row, col, level
babyshark = [0, 0, 2]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            babyshark[0], babyshark[1] = i, j

def get_next_fish(babyshark):
    global n
    queue = deque([[babyshark[0], babyshark[1], 0]])
    visited = set()
    visited.add((babyshark[0], babyshark[1]))
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    minimum = int(10e9)
    candidate = []
    while queue:
        x, y, mv = queue.popleft()
        if mv == minimum:
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n and \
               (nx, ny) not in visited and \
               matrix[nx][ny] <= babyshark[2]:
                queue.append([nx, ny, mv+1])
                visited.add((nx, ny))
                if matrix[nx][ny] != 0 and matrix[nx][ny] != 9 and \
                   matrix[nx][ny] < babyshark[2]:
                    minimum = mv+1
                    candidate.append([nx, ny])
    if candidate:
        candidate.sort(key=lambda x:(x[0], x[1]))
        return candidate[0][0], candidate[0][1], minimum
    else:
        return -1, -1, minimum
    

    
time = 0
eat_count = 0
while True:
    x, y, dist = get_next_fish(babyshark)
    if x == -1 and y == -1:
        break
    time += dist
    matrix[babyshark[0]][babyshark[1]] = 0
    babyshark[0], babyshark[1] = x, y
    matrix[babyshark[0]][babyshark[1]] = 9
    eat_count += 1
    if eat_count == babyshark[2]:
        babyshark[2] += 1
        eat_count = 0

print(time)
    

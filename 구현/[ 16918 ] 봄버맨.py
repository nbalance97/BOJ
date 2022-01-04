import sys

input = lambda: sys.stdin.readline().rstrip()
R, C, N = map(int, input().split())

matrix = [list(input()) for _ in range(R)]
boompos = []
for i in range(R):
    for j in range(C):
        if matrix[i][j] == 'O':
            boompos.append([i, j])

def set_boom(matrix):
    next_boom = set()
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '.':
                next_boom.add((i, j))
                matrix[i][j] = 'O'
    return next_boom

def boom(matrix, boompos, next_boom):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    destroypos = set()
    for x, y in boompos:
        destroypos.add((x, y))
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < R and 0 <= ny and ny < C:
                destroypos.add((nx, ny))

    for x, y in destroypos:
        if (x, y) in next_boom:
            next_boom.remove((x, y))
        matrix[x][y] = '.'
        

time = 1
while time < N:
    next_boom = set_boom(matrix)
    time += 1
    if time == N:
        break
    boom(matrix, boompos, next_boom)
    boompos = next_boom
    time += 1

for m in matrix:
    print("".join(m))

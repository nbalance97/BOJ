import sys
from collections import deque
import copy

input = lambda: sys.stdin.readline().rstrip()
R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]

N = int(input())
throws = map(int, input().split())

def bfs(matrix, sx, sy):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    block = [[sx, sy]]
    queue = deque([[sx, sy]])
    matrix[sx][sy] = '.'
    down = False if sx == R-1 else True
    while queue:
        sx, sy = queue.popleft()
        for i in range(4):
            nx, ny = sx + dx[i], sy + dy[i]
            if nx >= 0 and nx < R and ny >= 0 and ny < C and \
               matrix[nx][ny] == 'x':
                down = False if nx == R-1 else down
                block.append([nx, ny])
                queue.append([nx, ny])
                matrix[nx][ny] = '.'

    return block, down
    

def movedown(matrix, block):
    for x, y in block:
        matrix[x][y] = '.'
    movement_count = 0
    # 몇칸 이동해야하는지 구함
    for i in range(1, R):
        for x, y in block:
            if x+i+1 == R or matrix[x+i+1][y] == 'x':
                movement_count = i
                break
        if movement_count != 0:
            break

    for x, y in block:
        matrix[x+movement_count][y] = 'x'
    

def check(matrix):
    target = None
    cp_matrix = copy.deepcopy(matrix)
    for i in range(len(cp_matrix)):
        for j in range(len(cp_matrix[0])):
            if cp_matrix[i][j] == 'x':
                block, down = bfs(cp_matrix, i, j)
                if down:
                    target = block
                    break
        if target:
            break

    if target:
        movedown(matrix, target)

left = True
for throw in throws:
    if left:
        for j in range(C):
            if matrix[R-throw][j] == 'x':
                matrix[R-throw][j] = '.'
                break
    else:
        for j in range(C-1, -1, -1):
            if matrix[R-throw][j] == 'x':
                matrix[R-throw][j] = '.'
                break
    check(matrix)
    left = not left

for m in matrix:
    print("".join(m))

import sys
from collections import deque
import copy


input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def bfs(matrix, startX, startY):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque([[startX, startY]])
    block_color = matrix[startX][startY]
    matrix[startX][startY] = -1
    block_count = 1
    rainbow = []
    block = [[startX, startY]]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                if matrix[nx][ny] == block_color or matrix[nx][ny] == 0:
                    queue.append([nx, ny])
                    block.append([nx, ny])
                    block_count += 1
                    if matrix[nx][ny] == 0:
                        rainbow.append([nx, ny])
                    matrix[nx][ny] = -1

    for nx, ny in rainbow:
        matrix[nx][ny] = 0

    return block, block_count, len(rainbow)

def find_max_block(target):
    matrix = copy.deepcopy(target)
    max_block, max_block_count, max_rainbow = None, 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                block, block_count, rb_len = bfs(matrix, i, j)
                if max_block_count < block_count:
                    max_block, max_block_count, max_rainbow = block, block_count, rb_len
                elif max_block_count == block_count:
                    if max_rainbow <= rb_len:
                        max_block, max_block_count, max_rainbow = block, block_count, rb_len

    return max_block

def destroy(matrix, block):
    for x, y in block:
        matrix[x][y] = -2

def gravity(matrix):
    for i in range(len(matrix)-2, -1, -1):
        for j in range(len(matrix[0])):
            index = i
            if matrix[i][j] == -1:
                continue
            while index+1 != N and matrix[index+1][j] == -2:
                matrix[index+1][j] = matrix[index][j]
                matrix[index][j] = -2
                index += 1

def rotate(matrix):
    new_matrix = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_matrix[i][j] = matrix[j][len(matrix)-1-i]

    return new_matrix
            

score = 0

while True:
    block = find_max_block(matrix)
    if block == None:
        break
    if len(block) <= 1:
        break
    score += (len(block) ** 2)
    destroy(matrix, block)
    gravity(matrix)
    matrix = rotate(matrix)
    gravity(matrix)

print(score)

import sys
import copy
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

matrix = [list(map(int, input().split())) for _ in range(3)]

def find_0(matrix):
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                return [i, j]
    return None

def check_finish(matrix):
    answer = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    for i in range(3):
        for j in range(3):
            if answer[i][j] != matrix[i][j]:
                return False
    return True

def atos(matrix):
    result = ''
    for i in range(3):
        for j in range(3):
            result += str(matrix[i][j])
    return result

def stoa(string):
    return [[int(string[3*i+j]) for j in range(3)] for i in range(3)]

def bfs(matrix):
    visited = set([atos(matrix)])
    queue = deque()
    queue.append([atos(matrix), 0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        mat, movement = queue.popleft()
        mat = stoa(mat)
        if check_finish(mat):
            return movement
        x, y = find_0(mat)
        for i in range(4):
            target_x = x + dx[i]
            target_y = y + dy[i]
            if target_x >= 0 and target_x < 3 and target_y >= 0 and target_y < 3:
                mat[x][y], mat[target_x][target_y] = mat[target_x][target_y], mat[x][y]
                if atos(mat) not in visited:
                    visited.add(atos(mat))
                    queue.append([atos(mat), movement+1])
                mat[x][y], mat[target_x][target_y] = mat[target_x][target_y], mat[x][y]
    
    return -1

print(bfs(matrix))

import sys
from collections import deque as Deque

input = lambda: sys.stdin.readline().rstrip()
T = int(input())

def bfs(matrix, x, y):
    new_matrix = [[int(10e9)] * len(matrix[0]) for _ in range(len(matrix))]
    deque = Deque([[x, y]])
    dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
    R, C = len(matrix), len(matrix[0])
    visited = [[False] * C for _ in range(R)]
    visited[x][y] = True
    new_matrix[x][y] = 0
    while deque:
        cx, cy = deque.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx and nx < R and 0 <= ny and ny < C:
                if not visited[nx][ny] and matrix[nx][ny] == '.':
                    new_matrix[nx][ny] = new_matrix[cx][cy]
                    deque.appendleft([nx, ny])
                elif not visited[nx][ny] and matrix[nx][ny] == '#':
                    new_matrix[nx][ny] = new_matrix[cx][cy]+1
                    deque.append([nx, ny])
                visited[nx][ny] = True
    return new_matrix

for _ in range(T):
    h, w = map(int, input().split())
    matrix = [list('.'+input()+'.') for _ in range(h)]
    matrix = [['.'] * (w+2)] + matrix + [['.'] * (w+2)]
    player = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '$':
                player.append([i, j])
                matrix[i][j] = '.'
                
    playerA, playerB = player[0], player[1]
    matrix1 = bfs(matrix, 0, 0)
    matrix2 = bfs(matrix, playerA[0], playerA[1])
    matrix3 = bfs(matrix, playerB[0], playerB[1])

    answer = int(10e9)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '*':
                continue
            sumation = matrix1[i][j] + matrix2[i][j] + matrix3[i][j]
            if matrix[i][j] == '#':
                answer = min(answer, sumation-2)
            else:
                answer = min(answer, sumation)

    print(answer)

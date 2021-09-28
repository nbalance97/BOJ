import sys
import copy

from itertools import product

input = lambda : sys.stdin.readline().rstrip()
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

def up_down_movement(way, matrix):
    # way : 1, 2, 각각 위, 아래
    N = len(matrix)
    if way == 1:
        start, end, add = 0, N, 1
    elif way == 2:
        start, end, add = N-1, -1, -1

    new_matrix = [[0] * len(matrix) for _ in range(len(matrix))]
    for j in range(N):
        stack = []
        for i in range(start, end, add):
            if not stack and matrix[i][j] != 0:
                stack.append([matrix[i][j], False])
            elif stack and stack[-1][1] == False and stack[-1][0] == matrix[i][j]:
                latest, _ = stack.pop()
                stack.append([matrix[i][j] + latest, True])
            elif stack and matrix[i][j] != 0:
                stack.append([matrix[i][j], False])

        for i in range(len(stack)):
            if way == 1:
                new_matrix[i][j] = stack[i][0]
            elif way == 2:
                new_matrix[N-1-i][j] = stack[i][0]
                
    return new_matrix

def left_right_movement(way, matrix):
    # way가 각각 1,2일때 왼쪽, 오른쪽
    N = len(matrix)

    if way == 1:
        start, end, add = 0, N, 1
    elif way == 2:
        start, end, add = N-1, -1, -1

    new_matrix = [[0] * len(matrix) for _ in range(len(matrix))]
    for i in range(N):
        stack = []
        for j in range(start, end, add):
            if not stack and matrix[i][j] != 0:
                stack.append([matrix[i][j], False])
            elif stack and stack[-1][1] == False and stack[-1][0] == matrix[i][j]:
                latest, _ = stack.pop()
                stack.append([matrix[i][j] + latest, True])
            elif stack and matrix[i][j] != 0:
                stack.append([matrix[i][j], False])

        for j in range(len(stack)):
            if way == 1:
                new_matrix[i][j] = stack[j][0]
            elif way == 2:
                new_matrix[i][N-1-j] = stack[j][0]

    return new_matrix

def get_max(matrix):
    return max([max(q) for q in matrix])

ways = [list('ulrd') for _ in range(5)]

answer = 0
# 5번 모든 경우의 수 돌면서 이동시켜 봄.
for way in list(product(*ways)):
    new_matrix = matrix
    for each_way in way:
        if each_way == 'u':
            new_matrix = up_down_movement(1, new_matrix)
        elif each_way == 'd':
            new_matrix = up_down_movement(2, new_matrix)
        elif each_way == 'l':
            new_matrix = left_right_movement(1, new_matrix)
        elif each_way == 'r':
            new_matrix = left_right_movement(2, new_matrix)
        answer = max(answer, get_max(new_matrix))

print(answer)

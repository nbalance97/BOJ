import sys
import copy
from itertools import permutations

input = lambda : sys.stdin.readline().rstrip()
N, M, K = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def rotate(target, r, c, s):
    if s == 0:
        return
    r, c = r-1, c-1
    start_x, start_y = r-s, c-s
    end_x, end_y = r+s, c+s
    x, y = start_x, start_y
    first_value = target[start_x][start_y]
    
    for i in range(start_x, end_x):
        target[i][start_y] = target[i+1][start_y]

    for i in range(start_y, end_y):
        target[end_x][i] = target[end_x][i+1]

    for i in range(end_x, start_x, -1):
        target[i][end_y] = target[i-1][end_y]

    for i in range(end_y, start_y, -1):
        target[start_x][i] = target[start_x][i-1]
        
    target[start_x][start_y+1] = first_value
    rotate(target, r+1, c+1, s-1)

def get_max_sumation(target):
    return min([sum(q) for q in target])

rotate_information = []
rotate_idx = [i for i in range(K)]
rotate_sequence = list(permutations(rotate_idx, K))

for _ in range(K):
    rotate_information.append(list(map(int, input().split())))

answer = int(10e9)

for sequence in rotate_sequence:
    temp = copy.deepcopy(matrix)

    for i in sequence:
        r, c, s = rotate_information[i]
        rotate(temp, r, c, s)

    answer = min(answer, get_max_sumation(temp))
    
print(answer)

import sys
import copy
from collections import deque
from itertools import combinations

input = lambda : sys.stdin.readline().rstrip()

N, M, D = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

def movement_one_time(matrix):
    # 전체 배열 한칸씩 내림
    row, col = len(matrix), len(matrix[0])
    for j in range(col):
        for i in range(row-1, 0, -1):
            matrix[i][j] = matrix[i-1][j]

    for j in range(col):
        matrix[0][j] = 0

def kill_target(matrix, arthor_pos, attack_range):
    queue = deque([[arthor_pos[0], arthor_pos[1], 0]])
    visited = set((arthor_pos[0], arthor_pos[1]))
    ans_cost = -1
    dx = [0, -1, 0]
    dy = [-1, 0, 1]
    answer_list = []
    while queue:
        x, y, cost = queue.popleft()
        
        if cost == attack_range:
            continue
        
        if matrix[x][y] == 1:
            if ans_cost == -1:
                ans_cost = cost
                answer_list.append([x, y])
            else:
                if ans_cost == cost:
                    answer_list.append([x, y])
            continue

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < len(matrix) and 0 <= ny and ny < len(matrix[0]) and \
               (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append([nx, ny, cost+1])

    if len(answer_list) == 0:
        return None

    # 가장 왼쪽에 있는 적 찾는 부분
    min_left = int(10e9)
    min_index = 0
    for i in range(len(answer_list)):
        if answer_list[i][1] < min_left:
            min_index = i
            min_left = answer_list[i][1]
            
    target_x, target_y = answer_list[min_index]
    return [target_x, target_y]
                

all_case = list(combinations([i for i in range(M)], 3))

answer = 0
for case in all_case:
    test_matrix = copy.deepcopy(matrix)
    kill_count = 0
    for i in range(N):
        kill_set = set()
        for archor in case:
            P = kill_target(test_matrix, [N-1, archor], D)
            if P is not None:
                target_x, target_y = P
                kill_set.add((target_x, target_y))
        for x, y in kill_set:
            test_matrix[x][y] = 0
        kill_count += len(kill_set)
        movement_one_time(test_matrix)
    answer = max(answer, kill_count)

print(answer)

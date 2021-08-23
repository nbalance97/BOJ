import sys
import copy
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

def bfs(matrix, point, target):
    queue = deque([[point[0], point[1]]])
    visit = int(10e9)
    length = len(matrix)
    matrix[point[0]][point[1]] = visit
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < length and 0 <= ny and ny < length:
                if matrix[nx][ny] != visit and matrix[nx][ny] <= target:
                    matrix[nx][ny] = visit
                    queue.append([nx, ny])
    
answer = 0
for i in range(0, 101):
    temp_matrix = copy.deepcopy(matrix)
    
    # 잠기는 모든 부분 잠기도록 처리
    for j in range(N):
        for k in range(N):
            if temp_matrix[j][k] <= i:
                bfs(temp_matrix, [j, k], i)

    # 안잠긴 부분들 한 영역씩 잠기게 하면서 영역의 수 계산
    area_count = 0
    for j in range(N):
        for k in range(N):
            if temp_matrix[j][k] != int(10e9): 
                # 안잠긴 부분이 있다면 해당 영역 잠기도록
                area_count += 1
                bfs(temp_matrix, [j, k], int(10e9))

    answer = max(area_count, answer)

print(answer)

import sys
import copy
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
matrix = []
for _ in range(N):
    matrix.append(list(" ".join(input().rstrip()).split())) # 일반용

matrix2 = copy.deepcopy(matrix) # 적록색약용

def bfs(i, j, isrb):
    queue = deque()
    p = matrix[i][j]
    if isrb:
        p = matrix2[i][j]

    queue.append([i, j])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if x + dx[i] >= 0 and x + dx[i] < N and y + dy[i] >= 0 and y + dy[i] < N:
                if isrb:
                    # 적록색약인 경우 R, G를 하나로 묶어야 함
                    if p == "R" or p == "G":
                        if matrix2[x+dx[i]][y+dy[i]] == "R" or matrix2[x+dx[i]][y+dy[i]] == "G":
                            matrix2[x+dx[i]][y+dy[i]] = 'X'
                            queue.append([x+dx[i], y+dy[i]])
                    else:
                        if matrix2[x+dx[i]][y+dy[i]] == p:
                            matrix2[x+dx[i]][y+dy[i]] = 'X'
                            queue.append([x+dx[i], y+dy[i]])
                else:
                    # 아니면 그냥 단일색상으로만
                    if matrix[x+dx[i]][y+dy[i]] == p:
                        matrix[x+dx[i]][y+dy[i]] = 'X'
                        queue.append([x+dx[i], y+dy[i]])

                
count1, count2 = 0, 0

for i in range(N):
    for j in range(N):
        if matrix[i][j] != "X":
            bfs(i, j, False)
            count1 += 1
            
        if matrix2[i][j] != "X":
            bfs(i, j, True)
            count2 += 1

print(count1, count2)

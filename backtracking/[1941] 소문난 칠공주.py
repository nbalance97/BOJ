import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

idx = [[i, j] for i in range(5) for j in range(5)]
q = [list(input().rstrip()) for _ in range(5)]
comb = list(combinations(idx, 7))

def bfs(case):
    # 중복 체크를 위한 set
    total = set()
    visited = set()
    for c in case:
        total.add(tuple(c))
    # case 확인
    x1, y1 = case[0] # index 0에서 시작하도록
    queue = deque()
    queue.append([x1, y1])
    visited.add(tuple([x1, y1]))
    
    count_y = 0
    count_s = 0
    if q[x1][y1] == 'Y':
        count_y += 1
    else:
        count_s += 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < 5 and 0 <= ny and ny < 5:
                temp = tuple([nx, ny])
                if temp in total and temp not in visited:
                    if q[nx][ny] == 'Y':
                        count_y += 1
                    else:
                        count_s += 1
                    queue.append([nx, ny])
                    visited.add(temp)

    if count_y + count_s == 7 and count_s >= 4:
        return True
    else:
        return False
    
count = 0
for case in comb:
    if bfs(case):
        count += 1

print(count)
                
    

import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().rstrip().split())

def bfs(current):
    global F, G, U, D
    # 총 F층, G층이 목표, U칸 위, D칸 아래 가능
    
    visited = [False] * (F+1)
    queue = deque()
    visited[current] = True
    queue.append([current, 0])        

    while queue:
        stair, count = queue.popleft()
        if stair == G:
            return count
        if stair + U <= F and not visited[stair + U]:
            visited[stair + U] = True
            queue.append([stair + U, count+1])
        if stair - D > 0 and not visited[stair - D]:
            visited[stair - D] = True
            queue.append([stair - D, count+1])
        
    return -1
        


idx = bfs(S)
if idx == -1:
    print("use the stairs")
else:
    print(idx)

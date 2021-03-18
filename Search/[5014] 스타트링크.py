import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().rstrip().split())

def bfs(current):
    global F, G, U, D
    # 총 F층, G층이 목표, U칸 위, D칸 아래 가능
    
    visited = [False] * (F+1)
    queue = deque()
    # 현재 층 방문처리 및 queue에 삽입
    visited[current] = True
    queue.append([current, 0])        

    while queue:
        stair, count = queue.popleft()
        if stair == G:
            return count
        # 위층으로 방문한적이 없고, 이동 가능한 경우 방문처리 하고 queue에 넣음
        if stair + U <= F and not visited[stair + U]:
            visited[stair + U] = True
            queue.append([stair + U, count+1])
            
        # 아래층으로 방문한적이 없고, 이동 가능한 경우 방문처리 하고 queue에 넣음
        if stair - D > 0 and not visited[stair - D]:
            visited[stair - D] = True
            queue.append([stair - D, count+1])
        
    return -1
        


idx = bfs(S)
if idx == -1:
    print("use the stairs")
else:
    print(idx)

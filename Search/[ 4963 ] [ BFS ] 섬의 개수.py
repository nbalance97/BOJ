import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, x, y):
    queue = deque([[x, y]])
    graph[x][y] = 0
    # 상하좌우
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, 1, -1]

    # 대각선
    dx2 = [1, 1, -1, -1]
    dy2 = [-1, 1, -1, 1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            # 상하좌우
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx and nx < len(graph) and (
                0 <= ny and ny < len(graph[0])
            ):
               if graph[nx][ny] != 0:
                   graph[nx][ny] = 0
                   queue.append([nx, ny])
            # 대각선
            nx, ny = x+dx2[i], y+dy2[i]
            if 0 <= nx and nx < len(graph) and (
                0 <= ny and ny < len(graph[0])
            ):
                if graph[nx][ny] != 0:
                    graph[nx][ny] = 0
                    queue.append([nx,ny])
            
        
while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break
    
    graph = [list(map(int, input().rstrip().split())) for _ in range(h)]
    answer = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                answer += 1
                bfs(graph, i, j)
    print(answer)
            

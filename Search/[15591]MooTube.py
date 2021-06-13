import sys
from collections import deque

N, Q = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * (N+1)
graph = [[] for _ in range(N+1)]


def bfs(src, usado):
    for i in range(len(visited)):
        visited[i] = False

    queue = deque()
    queue.append([src, 9999999999])
    ucnt = 0
    visited[src] = True
    
    while queue:
        n, u = queue.popleft()
        if u >= usado and n != src:
            ucnt = ucnt + 1
            
        for nx, nu in graph[n]:
            if not visited[nx]:
                visited[nx] = True
                queue.append([nx, min(nu, u)])

    return ucnt
                
for i in range(N-1):
    p, q, r = map(int, sys.stdin.readline().rstrip().split())
    graph[p].append([q, r])
    graph[q].append([p, r])

for i in range(Q):
    usado, dest = map(int, sys.stdin.readline().rstrip().split())
    print(bfs(dest, usado))
        

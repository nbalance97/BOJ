import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    src, dest, cost = map(int, input().split())
    graph[src].append([dest, cost])
    graph[dest].append([src, cost])

def bfs(src, dest):
    queue = deque([[src, 0]])
    visited = [False] * (N+1)
    visited[src] = True
    target_cost = 0
    while queue:
        node, current_cost = queue.popleft()
        if node == dest:
            target_cost = current_cost
            break
        for next_node, next_cost in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append([next_node, current_cost + next_cost])

    return target_cost

for _ in range(M):
    src, dest = map(int, input().split())
    print(bfs(src, dest))

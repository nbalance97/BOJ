import sys
from collections import deque

input = sys.stdin.readline
N, M, k = map(int, input().rstrip().split())

costs = [0] + list(map(int, input().rstrip().split()))
visited = [False] * len(costs)

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

def get_min_cost(costs, visited):
    cost = int(10e9)
    idx = -1
    for i in range(1, len(costs)):
        if not visited[i] and cost > costs[i]:
            cost = costs[i]
            idx = i

    return (cost, idx)
total = 0
while True:
    cost, idx = get_min_cost(costs, visited)
    if idx == -1:
        print(total)
        sys.exit(0)

    total += cost
    
    if total > k:
        print("Oh no")
        sys.exit(0)
    
    queue = deque([idx])
    visited[idx] = True
    while queue:
        node = queue.popleft()
        for g in graph[node]:
            if not visited[g]:
                queue.append(g)
                visited[g] = True
                
    
    
    

import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
Tree =[[] for _ in range(10001)]

for _ in range(n-1):
    s, e, cost = map(int, input().rstrip().split())
    Tree[s].append([e, cost])
    Tree[e].append([s, cost])


def bfs(current):
    visited = [False] * 10001
    queue = deque()
    visited[current] = True
    queue.append([current, 0])

    cost = 0
    target = 0

    while queue:
        next_node, next_cost = queue.popleft()
        if next_cost > cost:
            cost = next_cost
            target = next_node

        for nx, cs in Tree[next_node]:
            if not visited[nx]:
                queue.append([nx, next_cost + cs])
                visited[nx] = True

    return cost, target

cost, target = bfs(1)
cost, _ = bfs(target)
print(cost)


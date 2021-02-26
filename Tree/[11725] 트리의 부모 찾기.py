import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
parent = [i for i in range(n+1)]
trees = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    s, e = map(int, input().rstrip().split())
    trees[s].append(e)
    trees[e].append(s)

current = 1
visited[current] = True

queue = deque()
queue.append(current)
while queue:
    current = queue.popleft()
    for next_node in trees[current]:
        if visited[next_node]:
            continue
        parent[next_node] = current
        visited[next_node] = True
        queue.append(next_node)

for i in range(2, n+1):
    print(parent[i])








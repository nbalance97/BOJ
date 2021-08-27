import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)

leap_depth = []
queue = deque([[1,0]])
visited = [False] * (N+1)
visited[1] = True
total_leaf_depth = 0
while queue:
    node, depth = queue.popleft()
    if len(tree[node]) == 1 and visited[tree[node][0]]:
        total_leaf_depth += depth
        continue

    for t in tree[node]:
        if not visited[t]:
            queue.append([t, depth+1])
            visited[t] = True


if total_leaf_depth % 2 == 1:
    print('Yes')
else:
    print('No')

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
N, W = map(int, input().split())
t = [[] for _ in range(N+1)]
v = [0] * (N+1)
v[1] = W

for _ in range(N-1):
    a, b = map(int, input().split())
    t[a].append(b)
    t[b].append(a)

visited = set()
visited.add(1)
queue = deque([1])

while queue:
    node = queue.popleft()
    count = 0
    for nx in t[node]:
        if nx not in visited:
            count += 1

    if count == 0:
        continue

    each_value = v[node] / count
    for nx in t[node]:
        if nx not in visited:
            v[nx] = each_value
            visited.add(nx)
            queue.append(nx)
    v[node] = 0

count = 0
for i in range(1, N+1):
    if v[i] != 0:
        count += 1

print(sum(v) / count)

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
solve_list = [0] * (N+1)

def bfs(visited, n):
    visited[n] = True
    queue = deque([n])
    count = 0
    while queue:
        x = queue.popleft()
        count += 1
        for nx in graph[x]:
            if not visited[nx]:
                visited[nx] = True
                queue.append(nx)
    return count

for _ in range(M):
    to_, from_ = map(int, input().split())
    graph[from_].append(to_)

for i in range(1, N+1):
    visited = [False] * (N+1)
    # visited를 set으로 구성하면 시간초과
    # 배열로 구성해야 시간초과 나지 않음..
    solve_list[i] = bfs(visited, i)
    
max_value = max(solve_list)
answer = []
for i in range(1, N+1):
    if solve_list[i] == max_value:
        answer.append(i)

print(*answer)

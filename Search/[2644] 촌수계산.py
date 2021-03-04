import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
p1, p2 = map(int, input().rstrip().split())
cnt = int(input().rstrip())

graph = [[] for _ in range(n+1)]

for _ in range(cnt):
    t1, t2 = map(int, input().rstrip().split())
    # 양쪽 관계이므로 둘다 append
    graph[t1].append(t2)
    graph[t2].append(t1)


def bfs(n, start, target):
    visited = [False] * (n+1)
    queue = deque()

    queue.append([start, 0])
    visited[start] = True

    while queue: # 큐가 빌때까지 진행
        next_node, step = queue.popleft()
        if next_node == target:
            return step

        for t in graph[next_node]:
            if not visited[t]: # 방문하지 않고, 연결되어 있는 사촌이라면 bfs 진행
                visited[t] = True
                queue.append([t, step + 1])

    return -1

print(bfs(n, p1, p2))
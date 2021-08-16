import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
semester = [0] * (N+1)
queue = deque()


for _ in range(M):
    src, dest = map(int, input().rstrip().split())
    graph[src].append(dest)
    indegree[dest] += 1

# 초기 진입차수가 0인 노드 등록 
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append([i, 1])

while queue:
    cur, sem = queue.popleft()
    semester[cur] = sem
    for n in graph[cur]:
        indegree[n] -= 1
        # 진입차수가 0이 되면 들을수 있는 과목이므로 넣어준다.
        if indegree[n] == 0:
            queue.append([n, sem+1])

print(*semester[1:])
            




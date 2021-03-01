import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    s, e = map(int, input().rstrip().split())
    graph[s].append(e)
    indegree[e] += 1 # 진입차수 저장

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0: # 진입차수가 0인 정점들을 queue에 저장함.(시작 가능)
        queue.append(i)

answer = []
while queue:
    node = queue.popleft()
    answer.append(node)
    for c in graph[node]:
        indegree[c] -= 1 # 연결된 간선들을 지움으로써 진입차수 줄임
        if indegree[c] == 0: # 진입차수가 0이 된다면 그 정점을 queue에 넣음
            queue.append(c)

for i in range(1, n+1): # 위상정렬 결과에 들지 않은 값들은 그냥 뒤에다가 붙여 줌
    if i not in answer:
        answer.append(i)

print(" ".join(map(str, answer)))

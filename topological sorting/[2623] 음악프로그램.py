import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

graph = [[0] * (N+1) for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    temp = list(map(int, input().rstrip().split()))
    temp = temp[1:]
    for i in range(1, len(temp)):
        if graph[temp[i-1]][temp[i]] != 1:
            graph[temp[i-1]][temp[i]] = 1
            indegree[temp[i]] += 1
        
candidate = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        candidate.append(i)

answer = []
while candidate:
    ni = candidate.popleft()
    answer.append(ni)

    for i in range(1, N+1):
        if graph[ni][i] == 1:
            indegree[i] -= 1
            if indegree[i] == 0:
                candidate.append(i)
                
if len(answer) == N:
    print("\n".join(list(map(str, answer))))
else:
    print(0)

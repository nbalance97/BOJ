import heapq
import sys

input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

solve = []
heap = []

for i in range(1, n+1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

while heap:
    problem_number = heapq.heappop(heap)
    solve.append(problem_number)
    for next_problem in graph[problem_number]:
        indegree[next_problem] -= 1
        if indegree[next_problem] == 0:
            heapq.heappush(heap, next_problem)

print(*solve)

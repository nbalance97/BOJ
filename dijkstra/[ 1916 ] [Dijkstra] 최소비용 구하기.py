import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    fr, to, cost = map(int, input().rstrip().split())
    graph[fr].append([cost, to])

A, B = map(int, input().rstrip().split())

INT_MAX = int(10e9)
heap = [[0, A]]
distance = [INT_MAX] * (N+1)
distance[A] = 0

while heap:
    cost, target = heapq.heappop(heap)
    if distance[target] < cost:
        continue
    for n_cost, n_node in graph[target]:
        if distance[n_node] > cost + n_cost:
            distance[n_node] = cost + n_cost
            heapq.heappush(heap, [cost + n_cost, n_node])

print(distance[B])

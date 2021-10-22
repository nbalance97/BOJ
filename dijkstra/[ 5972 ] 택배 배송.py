import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    src, dest, dist = map(int, input().split())
    graph[src].append([dest, dist])
    graph[dest].append([src, dist])

heap = []
distance = [int(10e9)] * (N+1)
distance[1] = 0
heapq.heappush(heap, [0, 1])

while heap:
    dist, node = heapq.heappop(heap)
    if distance[node] != dist:
        continue

    for dest, to in graph[node]:
        if distance[dest] > dist + to:
            distance[dest] = dist + to
            heapq.heappush(heap, [distance[dest], dest])

print(distance[N])

import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

heap = []
INT_MAX = int(10e9)
distance = [INT_MAX] * (N+1)
distance[1] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

heapq.heappush(heap, [0, 1])
while heap:
    dist, node = heapq.heappop(heap)
    if distance[node] != dist:
        continue

    for next_node in graph[node]:
        if distance[next_node] > dist + 1:
            distance[next_node] = dist + 1
            heapq.heappush(heap, [distance[next_node], next_node])

distance[0] = 0
max_distance = max(distance)
max_distance_number = distance.index(max_distance)
max_distance_count = distance.count(max_distance)
print(max_distance_number, max_distance, max_distance_count)
    

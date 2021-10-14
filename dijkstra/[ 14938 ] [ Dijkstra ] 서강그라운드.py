import sys
import heapq

INT_MAX = int(10e9)
input = lambda: sys.stdin.readline().rstrip()

n, m, r = map(int, input().split())
item_count = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append([b, l])
    graph[b].append([a, l])

answer = 0

for start in range(1, n+1):
    distance = [INT_MAX] * (n+1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, [start, 0])

    
    while heap:
        node, dist = heapq.heappop(heap)
        if distance[node] != dist:
            continue

        for next_node, next_distance in graph[node]:
            if distance[next_node] > distance[node] + next_distance:
                distance[next_node] = distance[node] + next_distance
                heapq.heappush(heap, [next_node, distance[next_node]])
    
    total_item_count = sum([item_count[i] for i in range(1, n+1) if distance[i] <= m])
    answer = max(answer, total_item_count)

print(answer)

import sys
import math
import heapq

input = sys.stdin.readline

n, w = map(int, input().split())
m = float(input())

xy = [list(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n + 1)]
already_made_set = set()

for _ in range(w):
    a, b = map(int, input().split())
    src, dest = min(a, b), max(a, b)
    already_made_set.add((src, dest))
    graph[src].append([dest, 0])
    graph[dest].append([src, 0])

# Graph에 대한 전처리 시작(존재하지 않는 간선들 모두 만들어 줌)
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if (i, j) not in already_made_set:
            a1 = xy[i - 1]
            a2 = xy[j - 1]
            dist = (a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2
            if m ** 2 >= dist:
                graph[i].append([j, math.sqrt(dist)])
                graph[j].append([i, math.sqrt(dist)])


# Dijkstra 알고리즘 사용하여 최단거리 구함
distance = [sys.maxsize] * (n + 1)
distance[1] = 0
heap = []
heapq.heappush(heap, [0, 1])

while heap:
    cost, node = heapq.heappop(heap)
    if cost != distance[node]:
        continue

    for next_node, dist in graph[node]:
        if cost + dist < distance[next_node]:
            distance[next_node] = cost + dist
            heapq.heappush(heap, [distance[next_node], next_node])

print(int(distance[n] * 1000))

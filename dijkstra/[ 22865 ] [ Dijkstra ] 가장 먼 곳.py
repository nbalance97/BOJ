import sys
import heapq

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
A, B, C = map(int, input().split())

graph = [[] for _ in range(N+1)]
M = int(input())

for _ in range(M):
    D, E, L = map(int, input().split())
    graph[D].append([E, L])
    graph[E].append([D, L])

def dijkstra(graph, start):
    INT_MAX = int(10e9)
    distance = [INT_MAX] * len(graph)
    distance[start] = 0
    heap = [[0, start]]
    while heap:
        dist, node = heapq.heappop(heap)
        if distance[node] != dist:
            continue

        for next_node, next_dist in graph[node]:
            if dist + next_dist < distance[next_node]:
                distance[next_node] = dist + next_dist
                heapq.heappush(heap, [distance[next_node], next_node])

    return distance

max_size = 0
answer = 0
dist_a = dijkstra(graph, A)
dist_b = dijkstra(graph, B)
dist_c = dijkstra(graph, C)

for i in range(1, N+1):
    if max_size < min(dist_a[i], dist_b[i], dist_c[i]):
        max_size = min(dist_a[i], dist_b[i], dist_c[i])
        answer = i
        
print(answer)


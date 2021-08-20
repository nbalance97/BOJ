import sys
from collections import deque
import heapq

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, weight = map(int, input().rstrip().split())
    graph[a].append([b, weight])
    graph[b].append([a, weight])

start, end = map(int, input().rstrip().split())

INT_MAX = int(10e9)
distance = [0] * (N+1)
heap = [[-INT_MAX, start]]
distance[start] = INT_MAX

while heap:
    cost, node = heapq.heappop(heap)
    cost = -cost
    
    # 이미 갱신된 경우라면 생략
    if distance[node] > cost:
        continue

    for next_node, next_cost in graph[node]:
        new_cost = min(cost, next_cost)
        # 기존 무게보다 현재 거쳤을때의 무게가 더 크다면 갱신
        if distance[next_node] < new_cost:
            distance[next_node] = new_cost
            heapq.heappush(heap, [-new_cost, next_node])

print(distance[end])
    
        

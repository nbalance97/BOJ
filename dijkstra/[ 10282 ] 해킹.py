import sys
import heapq

input = sys.stdin.readline

T = int(input().rstrip())
INT_MAX = int(10e9)

for _ in range(T):
    n, d, c = map(int,input().rstrip().split())
    graph = [[] for _ in range(n+1)]
    for __ in range(d):
        a, b, s = map(int, input().rstrip().split())
        graph[b].append([a, s])
    distance = [INT_MAX] * (n+1)
    distance[c] = 0
    heap = [[0, c]]
    while heap:
        cost, node = heapq.heappop(heap)
        if distance[node] != cost:
            continue
        
        for next_node, next_cost in graph[node]:
            if distance[next_node] > distance[node] + next_cost:
                distance[next_node] = distance[node] + next_cost
                heapq.heappush(heap, [distance[next_node], next_node])

    computer_count = 0
    time = 0
    for dist in distance:
        if dist != INT_MAX:
            computer_count += 1
            time = max(time, dist)

    print(computer_count, time)
    

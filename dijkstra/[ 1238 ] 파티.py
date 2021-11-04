import sys
import heapq

INT_MAX = int(10e9)

input = lambda: sys.stdin.readline().rstrip()
N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])

def dijkstra(X):
    heap = []
    time = [INT_MAX] * (N+1)
    time[X], time[0] = 0, 0
    heapq.heappush(heap, [0, X])

    while heap:
        curr_time, city = heapq.heappop(heap)
        if curr_time != time[city]:
            continue
        for e, t in graph[city]:
            if time[e] > t + curr_time:
                time[e] = t + curr_time
                heapq.heappush(heap, [time[e], e])

    return time

X_to_S = dijkstra(X)
answer = 0
for i in range(1, N+1):
    if i == X: continue
    answer = max(answer, dijkstra(i)[X] + X_to_S[i])

print(answer)

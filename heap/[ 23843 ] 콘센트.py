import sys
import heapq

N, M = map(int, input().split())
elec = list(map(int, input().split()))
elec.sort(reverse=True)
heap = []

for e in elec:
    if len(heap) < M:
        heapq.heappush(heap, e)
    else:
        outcome = heapq.heappop(heap)
        heapq.heappush(heap, outcome + e)

print(max(heap))

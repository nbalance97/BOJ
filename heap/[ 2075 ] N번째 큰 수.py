import sys
import heapq

heap = []
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for item in temp:
        heapq.heappush(heap, item)
    while len(heap) > N:
        heapq.heappop(heap)
print(heap[0])

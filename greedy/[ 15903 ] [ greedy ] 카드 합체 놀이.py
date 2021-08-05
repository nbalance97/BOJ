import sys
import heapq
 
n, m = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))
heap = []
 
for card in cards:
    heapq.heappush(heap, card)
 
for _ in range(m):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    heapq.heappush(heap, a+b)
    heapq.heappush(heap, a+b)
 
print(sum(heap))

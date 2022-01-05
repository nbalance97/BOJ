import sys
import heapq
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
stations = [list(map(int, input().split())) for _ in range(N)]
dist, current_gas = map(int, input().split())
heap = []

stations.sort(key=lambda x:x[0])
queue = deque(stations)

answer = 0
while True:
    while queue and queue[0][0] <= current_gas:
        _, gas  = queue.popleft()
        heapq.heappush(heap, -gas)

    if dist <= current_gas:
        break
    else:
        if not heap:
            answer = -1
            break
        append_gas = -heapq.heappop(heap)
        current_gas += append_gas
        answer += 1

print(answer)

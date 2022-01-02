import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
T = int(input())

for _ in range(T):
    K = int(input())
    L = list(map(int, input().split()))
    heapq.heapify(L)
    cost = 0
    while(len(L) > 1):
        element_1 = heapq.heappop(L)
        element_2 = heapq.heappop(L)
        cost += (element_1 + element_2)
        heapq.heappush(L, element_1 + element_2)

    print(cost)

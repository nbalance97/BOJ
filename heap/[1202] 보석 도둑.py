import sys
import heapq
 
input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
jewel = []
 
for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(jewel, [M, V])
 
backpack = [int(input()) for _ in range(K)]
backpack.sort()
 
jewel_value_heap = []
answer = 0
for b in backpack:
    # 현재 가방에서 가능한 보석 값들 최대 히프에 넣어줌
    while jewel and jewel[0][0] <= b:
        heapq.heappush(jewel_value_heap, -heapq.heappop(jewel)[1])
 
    # 최대 히프에서 값 하나 꺼내서 더해줌(현재 가방에 들어갈 보석)
    if jewel_value_heap:
        answer -= (heapq.heappop(jewel_value_heap))
 
print(answer)

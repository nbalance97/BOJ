import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
ht = [0] * 100001

max_heap, min_heap = [], []

for i in range(N):
    P, L = map(int, input().split())
    ht[P] = L

for i in range(len(ht)):
    if ht[i] != 0:
        heapq.heappush(min_heap, [ht[i], i])
        heapq.heappush(max_heap, [-ht[i], -i])
    
M = int(input())
for i in range(M):
    cmd = input().split()
    if cmd[0] == 'add':
        P, L = int(cmd[1]), int(cmd[2])
        ht[P] = L
        heapq.heappush(min_heap, [L, P])
        heapq.heappush(max_heap, [-L, -P])
    elif cmd[0] == 'recommend':
        c = int(cmd[1])
        idx = -1
        if c == 1:
            while True:
                target, idx = max_heap[0]
                target, idx = -target, -idx
                if ht[idx] != target:
                    heapq.heappop(max_heap)
                else:
                    break
        else:
            while True:
                target, idx = min_heap[0]
                if ht[idx] != target:
                    heapq.heappop(min_heap)
                else:
                    break
        print(idx)
    elif cmd[0] == 'solved':
        num = int(cmd[1])
        ht[num] = 0
        

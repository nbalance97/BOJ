import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

parent = [i for i in range(N+1)]

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    p1 = find(parent, a)
    p2 = find(parent, b)

    if p1 != p2:
        parent[p1] = p2

heap = []
for i in range(M):
    a, b, c = map(int, input().split())
    heapq.heappush(heap, [c, a, b])

answer = 0
count = 0
max_edge_value = 0
while heap:
    c, a, b = heapq.heappop(heap)
    if find(parent, a) != find(parent, b):
        answer += c
        max_edge_value = max(max_edge_value, c)
        union(parent, a, b)
        count += 1
    if count == N-1:
        break

print(answer - max_edge_value)

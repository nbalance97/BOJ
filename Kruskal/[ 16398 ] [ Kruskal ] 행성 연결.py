import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
heap = []
cost = [list(map(int,input().split())) for _ in range(N)]

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    p1 = find(parent, a)
    p2 = find(parent, b)
    if p1 != p2:
        parent[p1] = p2

for i in range(N):
    for j in range(i+1, N):
        heapq.heappush(heap, [cost[i][j], i, j])

answer = 0
parent = [i for i in range(N+1)]
edge_count = 0
while heap and edge_count < N-1:
    cost, fr, to = heapq.heappop(heap)
    if find(parent, fr) != find(parent, to):
        union(parent, fr, to)
        answer += cost
        edge_count += 1


print(answer)

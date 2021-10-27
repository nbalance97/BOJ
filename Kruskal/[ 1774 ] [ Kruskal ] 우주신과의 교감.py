import sys
import heapq
import math

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

def union(parent, a, b):
    pa = find(parent, a)
    pb = find(parent, b)

    if parent[pa] != parent[pb]:
        parent[pa] = parent[pb]

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])

    return parent[a]

pos = [[0, 0]]

parent = [i for i in range(N+1)]

for _ in range(1, N+1):
    x, y = map(int, input().split())
    pos.append([x, y])

for _ in range(M):
    a, b = map(int, input().split())
    if find(parent, a) != find(parent, b):
        union(parent, a, b)

heap = []

for i in range(1, N+1):
    for j in range(1, i):
        distance = math.sqrt((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2)
        heapq.heappush(heap, [distance, i, j])

answer = 0
while heap:
    dist, i, j = heapq.heappop(heap)
    if find(parent, i) != find(parent, j):
        answer += dist
        union(parent, i, j)
    else:
        continue

print("%.2f"%answer)

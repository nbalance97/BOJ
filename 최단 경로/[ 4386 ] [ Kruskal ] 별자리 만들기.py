import sys
import math
import heapq

input = sys.stdin.readline
n = int(input().rstrip())
stars = [[]]
for _ in range(n):
    x, y = map(float, input().rstrip().split())
    stars.append([x, y])

/* 각 점과 점 사이의 거리를 distance 배열에 담아둠. distance[i][j] : i점, j점 사이의 거리 */
distance = [[0] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            continue
        distance[i][j] = abs(math.sqrt(((stars[j][0] - stars[i][0]) ** 2) +
                                       ((stars[j][1] - stars[i][1]) ** 2)))

/* kruskal Algorithm 사용을 위해 heap에 distance에 따라 간선들 넣어 줌 */
heap = []
for i in range(1, n+1):
    for j in range(i+1, n+1):
        heapq.heappush(heap, [distance[i][j], i, j])

/* 사이클 방지를 위해 union-find 연산 수행 */
parent = [i for i in range(n+1)]
def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])

    return parent[a]

def union(parent, a, b):
    t1 = find(parent, a)
    t2 = find(parent, b)
    if t1 != t2:
        parent[t1] = parent[t2]

edge = 0
total = 0

/* kruskal Algorithm 실행 */
while heap:
    distance, i, j = heapq.heappop(heap)
    if find(parent, i) != find(parent, j):
        union(parent, i, j)
        total += distance
        edge += 1

    if edge == n-1:
        break

print(total)

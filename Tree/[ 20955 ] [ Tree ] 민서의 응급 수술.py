import sys

sys.setrecursionlimit(10**6)

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

answer = 0

for _ in range(M):
    a, b = map(int, input().split())
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
    else:
        answer += 1

parent_node = find(parent, 1)
idx = 1
for i in range(2, N+1):
    if find(parent, i) != parent_node:
        union(parent, i, idx)
        parent_node = find(parent, i)
        idx = i
        answer += 1

print(answer)
        
    


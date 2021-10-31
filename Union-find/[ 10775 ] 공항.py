import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**5)

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    p1 = find(parent, a)
    p2 = find(parent, b)
    if p1 < p2:
        parent[p2] = p1
    else:
        parent[p1] = p2

G = int(input().rstrip())
P = int(input().rstrip())
parent = [i for i in range(G+1)]
answer = 0

for i in range(P):
    ap = int(input().rstrip())
    where = find(parent, ap)
    if where == 0:
        break
    union(parent, where, where-1)
    answer += 1

print(answer)

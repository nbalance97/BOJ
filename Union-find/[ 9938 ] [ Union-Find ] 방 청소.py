import sys

input = lambda: sys.stdin.readline().rstrip()

N, L = map(int, input().split())
parent = [i for i in range(L+1)]
full = [False] * (L+1)
alcohol = [list(map(int, input().split())) for _ in range(N)]

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    t1 = find(parent, a)
    t2 = find(parent, b)
    if t1 < t2:
        parent[t2] = t1
    else:
        parent[t1] = t2

for a, b in alcohol:
    t1, t2 = find(parent, a), find(parent, b)
    if t1 != t2:
        union(parent, t1, t2)
        print("LADICA")
    else:
        if t1 == 0:
            print("SMECE")
        else:
            parent[t1] = 0
            print("LADICA")

import sys

sys.setrecursionlimit(10**6)
def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])

    return parent[a]

def union(parent, a, b):
    t1 = find(parent, a)
    t2 = find(parent, b)

    if t1 != t2:
        parent[t1] = parent[t2]

input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
parent = [i for i in range(n)]
for i in range(1, m+1):
    s, e = map(int, input().rstrip().split())
    if find(parent, s) != find(parent, e):
        union(parent, s, e)
    else:
        print(i)
        break
else:
    print(0)
import sys

sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
parent = [i for i in range(N+1)]


def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    par1 = find(parent, a)
    par2 = find(parent, b)

    if par1 != par2:
        parent[par1] = par2

for _ in range(N-2):
    a, b = map(int, input().split())
    if find(parent, a) != find(parent, b):
        union(parent, a, b)

for i in range(2, N+1):
    if find(parent, i) != find(parent, i-1):
        union(parent, i, i-1)
        print(i, i-1)

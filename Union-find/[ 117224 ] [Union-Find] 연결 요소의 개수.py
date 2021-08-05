import sys
 
N, M = map(int, sys.stdin.readline().rstrip().split())
 
parent = [i for i in range(N+1)]
def union(a, b):
    p1 = find(a)
    p2 = find(b)
    if p1 != p2:
        parent[p1] = p2
 
def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
 
    return parent[a]
 
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    if find(a) != find(b):
        union(a, b)
 
for i in range(1, N+1):
    find(i)
 
s = set(filter(lambda x:x>0, parent))
print(len(s))    

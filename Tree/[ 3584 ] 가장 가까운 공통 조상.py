import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

for _ in range(N):
    total_count = int(input())
    parent = [0] * (total_count + 1)
    for __ in range(total_count-1):
        p, c = map(int, input().split())
        parent[c] = p
    a1, a2 = map(int, input().split())
        
    pathA = []
    while a1 != 0:
        pathA.append(a1)
        a1 = parent[a1]
    
    pathB = set()
    while a2 != 0:
        pathB.add(a2)
        a2 = parent[a2]
        
    for p in pathA:
        if p in pathB:
            print(p)
            break

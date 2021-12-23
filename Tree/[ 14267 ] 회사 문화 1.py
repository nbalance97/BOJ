import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
parent = [0] + list(map(int, input().split()))
praise = [0] * len(parent)

for _ in range(M):
    i, w = map(int, input().split())
    praise[i] += w

for i in range(2, N+1):
    praise[i] += praise[parent[i]]

print(*(praise[1:]))

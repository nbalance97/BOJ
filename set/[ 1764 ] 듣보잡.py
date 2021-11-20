import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
N_set = set()
M_set = set()

for _ in range(N):
    N_set.add(input())
for _ in range(M):
    M_set.add(input())

P_set = list(N_set & M_set)
P_set.sort()
print(len(P_set))
for p in P_set:
    print(p)

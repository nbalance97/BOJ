import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
S = list(map(int, input().split()))
p = [0] * N
p[0] = S[0]

for i in range(1, len(S)):
    p[i] = p[i-1] + S[i]

p = [0] + p

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(p[b] - p[a-1])

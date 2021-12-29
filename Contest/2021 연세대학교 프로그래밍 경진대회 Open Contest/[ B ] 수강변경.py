import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

have = defaultdict(lambda: 0)
for a in A:
    have[a] += 1

count = 0
for b in B:
    if have[b] > 0:
        have[b] -= 1
    else:
        count += 1

print(count)

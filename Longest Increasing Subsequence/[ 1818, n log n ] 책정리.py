import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
lcs = []

for a in arr:
    if not lcs or lcs[-1] < a:
        lcs.append(a)
        continue
    lower_bound = bisect_left(lcs, a)
    lcs[lower_bound] = a


print(n - len(lcs))

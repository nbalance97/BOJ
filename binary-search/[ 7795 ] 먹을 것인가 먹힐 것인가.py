import sys
from bisect import bisect_left


input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    T1 = sorted(map(int, input().split()))
    T2 = sorted(map(int, input().split()))
    count = 0
    for e1 in T1:
        pos = bisect_left(T2, e1)
        count += pos
    print(count)

from bisect import bisect_left, bisect_right
import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
points = list(map(int, sys.stdin.readline().rstrip().split()))
points.sort()

for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    lidx = bisect_left(points, a)
    ridx = bisect_right(points, b)
    print(ridx - lidx)

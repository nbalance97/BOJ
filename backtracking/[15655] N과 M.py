import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

num = list(map(int, input().rstrip().split()))
num.sort()

com = combinations(num, M)

for t in com:
    for q in t:
        print(q, end=" ")
    print()

import sys
from itertools import permutations

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

num = list(map(int, input().rstrip().split()))
num.sort()

per = permutations(num, M)

for t in per:
    for q in t:
        print(q, end=" ")
    print()

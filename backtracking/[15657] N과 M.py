import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

num = list(map(int, input().rstrip().split()))
num.sort()

com = combinations_with_replacement(num, M) # 중복조합

for t in com:
    for q in t:
        print(q, end=" ")
    print()

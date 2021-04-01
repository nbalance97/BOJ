import sys
from itertools import product

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

num = list(map(int, input().rstrip().split()))
num.sort()

com = product(num, repeat=M) # 중복순열

for t in com:
    for q in t:
        print(q, end=" ")
    print()

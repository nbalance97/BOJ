import sys
from itertools import permutations

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

num = list(map(int, input().rstrip().split()))
num.sort()
com = list(set(permutations(num, M)))
com.sort()
answer = []
# 중복 제거를 set으로 하면 속도가 훨씬 빠르다.
# in 연산자보다 훨 빠름.

for t in com:
    for q in t:
        print(q, end=" ")
    print()

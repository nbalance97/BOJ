import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input().rstrip())
sequence = [i+1 for i in range(N)]

total_case = list(permutations(sequence, N))
for case in total_case:
    print(*case)

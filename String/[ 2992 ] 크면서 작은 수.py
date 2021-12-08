import sys
from itertools import permutations

input = lambda: sys.stdin.readline().rstrip()
P = list(input())

answer = int(10e9)
original = int("".join(P))

for case in permutations(P):
    temp = int("".join(case))
    if temp > original and answer > temp:
        answer = temp

if answer == int(10e9):
    print(0)
else:
    print(answer)

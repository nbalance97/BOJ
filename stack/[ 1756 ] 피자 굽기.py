import sys
from collections import deque

input = sys.stdin.readline
d, n = map(int, input().split())
ovens = list(map(int, input().split()))
pizzas = list(map(int, input().split()))

for i in range(len(ovens) - 1):
    if ovens[i] < ovens[i+1]:
        ovens[i+1] = ovens[i]

ovens = deque(ovens)
depth = len(ovens)
answer = -1
count = 0

for pizza in pizzas:
    while ovens and (floor := ovens.pop()) != 0:
        if floor >= pizza:
            answer = depth
            count += 1
            depth -= 1
            break
        depth -= 1

if count != len(pizzas):
    print(0)
else:
    print(answer)



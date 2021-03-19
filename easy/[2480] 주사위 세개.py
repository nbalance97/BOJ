import sys

a, b, c = map(int, sys.stdin.readline().rstrip().split())

total = 0
if a == b and b == c:
    total = 10000 + a * 1000
else:
    if a == b:
        total = 1000 + a * 100
    elif b == c:
        total = 1000 + b * 100
    elif a == c:
        total = 1000 + a * 100
    else:
        total = max(a, b, c) * 100

print(total)


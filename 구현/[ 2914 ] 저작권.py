import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())
current = a * (b-1)

while True:
    if math.ceil(current / a) == b:
        break
    current += 1

print(current)

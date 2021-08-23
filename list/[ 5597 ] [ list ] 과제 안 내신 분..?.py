import sys

input = sys.stdin.readline

p = [int(input().rstrip()) for _ in range(28)]
for i in range(1, 31):
    if i not in p:
        print(i)

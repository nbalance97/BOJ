import sys

input = lambda: sys.stdin.readline().rstrip()
T = int(input())

for _ in range(T):
    N = int(input())
    if N % 3 == 2 or N % 9 == 0:
        print("TAK")
    else:
        print("NIE")

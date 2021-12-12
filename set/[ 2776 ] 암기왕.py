import sys

input = lambda: sys.stdin.readline().rstrip()
T = int(input())

for _ in range(T):
    N1 = int(input())
    diaryA = set(list(map(int, input().split())))
    N2 = int(input())
    diaryB = list(map(int, input().split()))
    for b in diaryB:
        if b in diaryA:
            print(1)
        else:
            print(0)

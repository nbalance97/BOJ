import sys

input = lambda: sys.stdin.readline().rstrip()
G = int(input())
left = 1
right = 2
answer = 0
while left < right:
    p = right ** 2 - left ** 2

    if p == G:
        answer += 1
        print(right)

    if p > G:
        left += 1
    else:
        right += 1


if answer == 0:
    print(-1)

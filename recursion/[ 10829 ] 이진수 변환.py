import sys

input = lambda : sys.stdin.readline().rstrip()

n = int(input())

def solve(p):
    if p == 0:
        return ""

    return solve(p//2) + str(p%2)

print(solve(n))

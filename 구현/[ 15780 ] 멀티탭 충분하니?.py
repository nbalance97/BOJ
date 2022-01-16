import sys

input = lambda: sys.stdin.readline()

N, K = map(int, input().split())
code = list(map(int, input().split()))

total_code = sum([c // 2 for c in code if c % 2 == 0])
total_code += sum([c // 2 + 1 for c in code if c % 2 == 1])
if total_code >= N:
    print('YES')
else:
    print('NO')

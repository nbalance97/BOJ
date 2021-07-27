import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [numbers[0]] + [0] * (n-1)

for i in range(1, n):
    dp[i] = dp[i-1] + numbers[i]

for i in range(m):
    src, dest = map(int, sys.stdin.readline().rstrip().split())
    src = src - 1
    dest = dest - 1
    if src == 0:
        print(dp[dest])
    else:
        print(dp[dest]-dp[src-1])
    
    

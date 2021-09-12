import sys

N = int(sys.stdin.readline().rstrip())

coins = [1, 2, 5, 7]

INT_MAX = int(10e9)
dp = [INT_MAX] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    for c in coins:
        if i - c < 0:
            break
        dp[i] = min(dp[i], dp[i-c] + 1)

print(dp[N])

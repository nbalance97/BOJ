import sys

n = int(sys.stdin.readline().rstrip())
INF = int(10e9)
dp = [INF] * (n+1)
dp[0] = 0

for i in range(1, n+1):
    if i-2 >= 0:
        dp[i] = min(dp[i], dp[i-2]+1)
    if i-5 >= 0:
        dp[i] = min(dp[i], dp[i-5]+1)


if dp[n] == INF:
    print(-1)
else:
    print(dp[n])

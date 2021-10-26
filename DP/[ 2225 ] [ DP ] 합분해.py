import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
dp = [[0] * (M+1) for i in range(N+1)]

for i in range(M+1):
    dp[0][i] = 1

for i in range(1, N+1):
    for j in range(1, M+1):
        for k in range(0, i+1):
            dp[i][j] += dp[k][j-1]
        dp[i][j] = dp[i][j] % 1000000000

print(dp[N][M])
    


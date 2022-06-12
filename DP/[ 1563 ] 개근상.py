import sys

input = sys.stdin.readline
n = int(input().rstrip())
dp = [[[0] * 2 for __ in range(3)] for _ in range(n+1)]
dp[1][0][0] = 1
dp[1][0][1] = 1
dp[1][1][0] = 1

DIVISOR = 1000000

for i in range(2, n+1):
    dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0]) % DIVISOR
    dp[i][0][1] = (dp[i][0][0] + dp[i-1][0][1] + dp[i-1][1][1] +  dp[i-1][2][1]) % DIVISOR
    dp[i][1][0] = dp[i-1][0][0] % DIVISOR
    dp[i][1][1] = dp[i-1][0][1] % DIVISOR
    dp[i][2][0] = dp[i-1][1][0] % DIVISOR
    dp[i][2][1] = dp[i-1][1][1] % DIVISOR

answer = 0
for i in range(3):
    answer += sum(dp[n][i])

print(answer % DIVISOR)

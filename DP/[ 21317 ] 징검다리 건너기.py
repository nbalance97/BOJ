import sys
from collections import deque

N = int(input().rstrip())

small = [0] * (N+1)
big = [0] * (N+1)

for i in range(1, N):
    a, b = map(int, input().rstrip().split())
    small[i], big[i] = a, b

K = int(input().rstrip())

INT_MAX = int(10e9)
dp = [[INT_MAX] * 2 for _ in range(N+1)]
dp[1][0], dp[1][1] = 0, INT_MAX
for i in range(1, N):
    dp[i+1][0] = min(dp[i+1][0], dp[i][0]+small[i])
    dp[i+1][1] = min(dp[i+1][1], dp[i][1]+small[i])
    if i + 2 <= N:
        dp[i+2][0] = min(dp[i+2][0], dp[i][0]+big[i])
        dp[i+2][1] = min(dp[i+2][1], dp[i][1]+big[i])
    if i + 3 <= N:
        dp[i+3][1] = min(dp[i+3][1], dp[i][0] + K)


print(min(dp[N]))

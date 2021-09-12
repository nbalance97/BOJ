import sys

N = int(input())
cards = list(map(int, input().split()))

INT_MAX = int(10e9)
dp = [INT_MAX] * (N+1)
dp[0] = 0

for i in range(1, N+1):
    for idx, card in enumerate(cards):
        if i - (idx + 1) >= 0:
            dp[i] = min(dp[i], dp[i-(idx+1)] + card)

print(dp[N])

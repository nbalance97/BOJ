import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

fixed = sorted([int(input()) for _ in range(M)])

dp = [0] * (N + 10)
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1
last = 0
for idx, fix in enumerate(fixed):
    if idx == 0:
        answer *= dp[fix - 1]
    else:
        answer *= dp[fix - fixed[idx - 1] - 1]
    last = fix

answer *= dp[N - last]

print(answer)

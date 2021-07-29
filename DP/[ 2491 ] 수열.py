import sys

input = sys.stdin.readline

n = int(input().rstrip())
sequence = list(map(int, input().rstrip().split()))

down_dp = [1] * n
up_dp = [1] * n

for i in range(1, n):
    if sequence[i-1] <= sequence[i]:
        up_dp[i] = up_dp[i-1] + 1
    if sequence[i-1] >= sequence[i]:
        down_dp[i] = down_dp[i-1] + 1

print(max(max(up_dp), max(down_dp)))

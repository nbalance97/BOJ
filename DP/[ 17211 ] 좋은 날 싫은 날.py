import sys

input = lambda : sys.stdin.readline().rstrip()

N, today = map(int, input().split())
percentage = list(map(float, input().split()))
dp = [[0] * 2 for _ in range(101)]

if today == 0:
    dp[0][0] = 1
else:
    dp[0][1] = 1


for i in range(1, N+1):
    dp[i][0] = dp[i-1][0] * percentage[0] + dp[i-1][1] * percentage[2]
    dp[i][1] = dp[i-1][0] * percentage[1] + dp[i-1][1] * percentage[3]

negative = round(dp[N][1] * 1000, 1)
positive = round(dp[N][0] * 1000, 1)

print(int(positive))
print(int(negative))

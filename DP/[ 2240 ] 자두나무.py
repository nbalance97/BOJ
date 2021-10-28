import sys

input = lambda: sys.stdin.readline().rstrip()

T, W = map(int, input().split())

dp = [[[0] * 3 for _ in range(W+1)] for _ in range(T+1)]
jadoo = [int(input()) for _ in range(T)]

if jadoo[0] == 1:
    dp[1][0][1] = 1
else:
    dp[1][1][2] = 1


for i in range(1, len(jadoo)):
    idx = i+1
    target = jadoo[i]
    for j in range(W+1):
        if j == 0:
            dp[idx][j][1] = dp[idx-1][j][1]
            dp[idx][j][2] = dp[idx-1][j][2]
        else:
            dp[idx][j][1] = max(dp[idx-1][j-1][2], dp[idx-1][j][1])
            dp[idx][j][2] = max(dp[idx-1][j-1][1], dp[idx-1][j][2])
            
        dp[idx][j][target] += 1

answer = 0
for i in range(W+1):
    for j in range(1, 3):
        if dp[T][i][j] >= answer:
            answer = dp[T][i][j]

print(answer)

import sys

input = sys.stdin.readline

N = int(input().rstrip())
dp = [[0] * 10 for _ in range(N+1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] = (dp[i][j] + dp[i-1][k]) % 10007

answer = sum(dp[N]) % 10007

print(answer)
    
        

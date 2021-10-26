import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1])
        if i-1 >= 0 and j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1])
        
        dp[i][j] += matrix[i][j]
        
print(dp[N-1][M-1])

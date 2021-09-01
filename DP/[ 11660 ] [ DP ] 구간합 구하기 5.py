import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

matrix = ([[0] * (N+1)]) + (
    [[0] + list(map(int, input().rstrip().split())) for _ in range(N)]
) 
dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][1] = dp[i-1][1] + matrix[i][1]
    dp[1][i] = dp[1][i-1] + matrix[1][i]

for i in range(2, N+1):
    for j in range(2, N+1):
        dp[i][j] = matrix[i][j] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    area = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]
    print(area)

import sys

input = sys.stdin.readline
N = int(input().rstrip())

matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0:
            continue
        if i + matrix[i][j] < N:
            dp[i+matrix[i][j]][j] += dp[i][j]
        if j + matrix[i][j] < N:
            dp[i][j+matrix[i][j]] += dp[i][j]  

print(dp[N-1][N-1])

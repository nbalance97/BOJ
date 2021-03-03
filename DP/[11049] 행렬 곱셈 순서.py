import sys

input = sys.stdin.readline

n = int(input().rstrip())

matrix = [[0, 0]]
for _ in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

INT_MAX = sys.maxsize
dp = [[INT_MAX] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 0

for phase in range(1, n+1):
    for start in range(1, n + 1 - phase):
        end = start + phase
        for j in range(start, end):
            cost = dp[start][j] + dp[j+1][end] + matrix[start][0] * matrix[j][1] * matrix[end][1]
            if cost < dp[start][end]:
                dp[start][end] = cost

print(dp[1][n])

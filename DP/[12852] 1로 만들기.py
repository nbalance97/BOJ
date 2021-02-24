import sys
INT_MAX = sys.maxsize

input = sys.stdin.readline

N = int(input().rstrip())
dp = [[INT_MAX] * 2 for _ in range(N+1)] # 열에 dp값과 이전값 동시 저장
dp[1][0] = 0
dp[1][1] = 0

for i in range(1, N):
    if i * 2 <= N and dp[i * 2][0] > dp[i][0] + 1:
        dp[i * 2][0] = dp[i][0] + 1
        dp[i * 2][1] = i
    if i * 3 <= N and dp[i * 3][0] > dp[i][0] + 1:
        dp[i * 3][0] = dp[i][0] + 1
        dp[i * 3][1] = i
    if dp[i+1][0] > dp[i][0] + 1:
        dp[i+1][0] = dp[i][0] + 1
        dp[i+1][1] = i

print(dp[N][0])
current = N
while True:
    print(current, end=" ")
    if current == 1: break
    current = dp[current][1]
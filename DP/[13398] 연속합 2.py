N = int(input())
temp = list(map(int, input().split()))

dp = [[0, 0] for _ in range(N)]
dp[0][0], dp[0][1] = temp[0], 0


m = -int(10e9)
for i in range(1, N):
    dp[i][0] = max(temp[i], dp[i-1][0] + temp[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + temp[i])

if N == 1:
    print(temp[0])
else:
    for i in range(1, N):
        m = max(m, dp[i][0], dp[i][1])
    m = max(m, dp[0][0])
    print(m)
    

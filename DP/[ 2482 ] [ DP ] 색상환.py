import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
K = int(input())

answer = 0
selected = True

div = 1000000003
for i in range(2):
    dp = [[0] * (K+1) for _ in range(N+1)]
    for i in range(1, N+1):
        if not selected:
            dp[i][1] = i-1
            dp[i][0] = 1
        else:
            dp[i][1] = 1
            dp[i][0] = 0

    for i in range(2, N+1):
        for j in range(2, K+1):
            dp[i][j] += dp[i-1][j]
            if i >= 2 and j >= 1:
                dp[i][j] += dp[i-2][j-1]

            dp[i][j] %= div

    if selected:
        answer += dp[N-1][K]
    else:
        answer += dp[N][K]
        
    answer %= div
    selected = not selected
    
print(answer)

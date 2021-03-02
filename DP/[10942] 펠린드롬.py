import sys

input = sys.stdin.readline
N = int(input().rstrip())
number = [0] + list(map(int, input().rstrip().split()))

dp = [[0] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][i] = 1
    if i + 1 <= N:
        if number[i] == number[i+1]:
            dp[i][i+1] = 1

for i in range(N, 0, -1):
    for j in range(i+2, N+1):
        if dp[i+1][j-1] == 1 and number[i] == number[j]:
            dp[i][j] = 1
            
n_size = int(input().rstrip())
for _ in range(n_size):
    s, e = map(int, input().rstrip().split())
    print(dp[s][e])

import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
T = [0]
P = [0]

for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

dp = [0] * (N+2)

for i in range(1, N+2):
    dp[i] = max(dp[i-1], dp[i])
    if i == N+1:
        break
    if i + T[i] <= N+1:
        dp[i+T[i]] = max(dp[i+T[i]], dp[i] + P[i])

print(max(dp))

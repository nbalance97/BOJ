import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
M = int(input())
VIP = set([int(input()) for _ in range(M)])
dp = [0] * (N+1)
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

count = 0
answer = 1
for i in range(1, N+1):
    if i in VIP:
        if count > 0:
            answer *= dp[count]
        count = 0
    else:
        count += 1

if count != 0:
    answer *= dp[count]

print(answer)

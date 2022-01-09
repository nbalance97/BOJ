import sys

input = lambda: sys.stdin.readline().rstrip()
dp = [0] * 1000001
dp[0] = 1
myuk = [2**i for i in range(20)]

N = int(input())
for m in myuk:
    for n in range(m, 1000001):
        dp[n] += dp[n-m]
        dp[n] %= 1000000000
print(dp[N])

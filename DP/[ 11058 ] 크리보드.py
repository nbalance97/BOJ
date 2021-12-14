import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
DP = [0] * 101

for i in range(1, 100):
    DP[i] = max(DP[i], DP[i-1] + 1)
    for j in range(i+3, 101):
        DP[j] = max(DP[j],
                    DP[j-3] + DP[i],
                    DP[i] + DP[i] * (j-i-2))

print(DP[N])

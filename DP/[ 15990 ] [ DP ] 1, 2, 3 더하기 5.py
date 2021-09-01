import sys

input = sys.stdin.readline
T = int(input().rstrip())

# dp[i][j] : i번째에 마지막으로 숫자가 j인 경우
dp = [[0, 1, 1, 1], [0, 1, 0, 0], [0, 0, 1, 0], [0, 1, 1, 1]] + (
    [[0] * 4 for _ in range(100001)]
)

for i in range(4, 100001):
    for j in [1, 2, 3]:
        for k in range(1, 4):
            # 이전에 나온 숫자를 바로 다시 나오게 하면 안됨.
            if j != k:
                dp[i][j] = (dp[i][j] + dp[i-j][k]) % 1000000009

for _ in range(T):
    n = int(input().rstrip())
    print(sum(dp[n]) % 1000000009)

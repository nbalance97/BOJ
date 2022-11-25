import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

matrix = []
for _ in range(n):
    matrix.append(input().rstrip())

dp = [[[0] * 100 for _ in range(m)] for __ in range(n)]


def make_table(target_word):
    global k, n, m

    for idx, ch in enumerate(target_word):
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != ch:
                    continue
                if idx == 0:
                    dp[i][j][idx+1] = 1

                for p in range(1, k + 1):
                    if i-p >= 0:
                        dp[i][j][idx+1] += dp[i - p][j][idx]

                    if i+p < n:
                        dp[i][j][idx+1] += dp[i + p][j][idx]

                    if j-p >= 0:
                        dp[i][j][idx+1] += dp[i][j - p][idx]

                    if j+p < m:
                        dp[i][j][idx+1] += dp[i][j + p][idx]


target_word = input().rstrip()
make_table(target_word)
answer = 0
for i in range(n):
    for j in range(m):
        answer += dp[i][j][len(target_word)]

print(answer)

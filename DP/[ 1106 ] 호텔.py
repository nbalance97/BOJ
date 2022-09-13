import sys

input = sys.stdin.readline
c, n = map(int, input().split())

INT_MAX = sys.maxsize
cost = [list(map(int, input().split())) for _ in range(n)]
cost.sort(key=lambda x: x[1])
dp = [INT_MAX] * (c+101)
dp[0] = 0

for i in range(1, c+101):
    for current_cost, people_count in cost:
        if i - people_count >= 0:
            dp[i] = min(dp[i], dp[i - people_count] + current_cost)
        else:
            break

print(min(dp[c:]))


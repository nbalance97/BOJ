import sys

input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
blocks = list(map(int, input().split()))

dp = [0] * (N+1)
dp[N] = 1

area = []
for idx, block in enumerate(blocks):
    if block > K:
        dp[idx+1] = 0
        area.append(dp[idx])
    else:
        dp[idx+1] = dp[idx] + 1
        
if blocks[-1] <= K:
    area.append(dp[N-1])

answer = 0
max_value = 0

if len(area) == 0:
    answer = 1
elif len(area) == 1:
    if area[-1] == len(blocks):
        answer = area[-1] + 1
    else:
        answer = area[-1] + 2
else:
    for i in range(1, len(area)):
        dist = area[i] + area[i-1]
        max_value = max(max_value, dist + 2)
    answer = max_value

print(answer)
        

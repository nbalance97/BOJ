
n = int(input())
boxes = list(map(int, input().split()))

dp = [1] * len(boxes)

for i in range(len(boxes)):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))

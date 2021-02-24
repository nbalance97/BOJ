import sys
INT_MAX = sys.maxsize

input = sys.stdin.readline
input1 = [" "] + list(" ".join(input().rstrip()).split())
input2 = [" "] + list(" ".join(input().rstrip()).split())

l1 = len(input1)
l2 = len(input2)

dp = [[0] * (l1) for _ in range(l2)]
log = [[""] * (l1) for _ in range(l2)]

for j in range(1, l1):
    for i in range(1, l2):
        if dp[i-1][j] > dp[i][j-1]:
            dp[i][j] = dp[i-1][j]
            log[i][j] = log[i-1][j]
        else:
            dp[i][j] = dp[i][j-1]
            log[i][j] = log[i][j-1]

        if input1[j] == input2[i]:
            if dp[i][j] < dp[i-1][j-1] + 1:
                dp[i][j] = dp[i-1][j-1] + 1
                log[i][j] = log[i-1][j-1] + input1[j]

print(dp[l2-1][l1-1])
if dp[l2-1][l1-1] > 0:
    print(log[l2-1][l1-1])

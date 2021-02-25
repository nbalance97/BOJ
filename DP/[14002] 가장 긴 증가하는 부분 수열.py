import sys
INT_MAX = sys.maxsize

input = sys.stdin.readline
count = int(input().rstrip())
sequence = list(map(int, input().rstrip().split()))

dp = [0] * count
pre = [0] * count
dp[0] = 1

for i in range(1, count):
    for j in range(0, i):
        if sequence[i] > sequence[j] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            pre[i] = j
    if dp[i] == 0:
        dp[i] = 1
        pre[i] = i

p = 0 # 정답 찾는 과정(dp값이 최대인걸 찾아야 함)
for i in range(1, count):
    if dp[p] < dp[i]:
        p = i

print(dp[p])

answer = []
current = p
while current != pre[current]:
    answer.append(sequence[current])
    current = pre[current]
answer.append(sequence[current])


print(" ".join(list(map(str, answer[::-1]))))
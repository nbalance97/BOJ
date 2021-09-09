N = int(input())
temp = list(map(int, input().split()))

dp = [i for i in temp]

for i in range(N):
    for j in range(i):
        if temp[i] > temp[j]:
            dp[i] = max(dp[i], dp[j] + temp[i])

print(max(dp))

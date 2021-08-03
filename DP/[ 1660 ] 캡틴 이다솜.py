N = int(sys.stdin.readline().rstrip())
curr = 1
step = 1
k = 1
area = 1
INT_MAX = int(10e9)
dp = [INT_MAX] * 300001
four = [1]
dp[1] = True
dp[0] = True
# 사면체 경우의 수 구하는 부분
while True:
    if N == area:
        print(1)
        sys.exit(0)
    if N < area:
        break
    k += 1
    curr += k
    area += curr
    four.append(area)
    if area <= 300000:
        dp[area] = 1
        
# dp 테이블 채우는 부분
for i in range(1, N+1):
    for j in four:
        if i - j > 0:
            dp[i] = min(dp[i], dp[i-j]+1)

print(dp[N])

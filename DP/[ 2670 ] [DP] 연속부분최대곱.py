import sys
 
input = sys.stdin.readline
 
N = int(input().rstrip())
numbers = [float(input().rstrip()) for _ in range(N)]
dp = [0] * N
 
dp[0] = numbers[0]
 
for i in range(N):
    if i > 0:
        dp[i] = max(dp[i-1] * numbers[i], numbers[i])
 
print("%.3f"%(round(max(dp), 3)))

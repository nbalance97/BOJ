import sys

sys.setrecursionlimit(10**5)
N, K = map(int, sys.stdin.readline().rstrip().split())


dp = [[-1] * 1001 for _ in range(1001)]

def solve(i, j):
    if i == j or j == 0:
        dp[i][j] = 1
        
    if dp[i][j] == -1:
        dp[i][j] = (solve(i-1, j-1) % 10007  + solve(i-1, j) % 10007) % 10007
        
    return dp[i][j]

print(solve(N, K))

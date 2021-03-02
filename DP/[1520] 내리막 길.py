import sys

sys
input = sys.stdin.readline
M, N = map(int, input().rstrip().split())
dp = [[-1] * N for _ in range(M)]
Map = []
for _ in range(M):
    Map.append(list(map(int, input().rstrip().split())))
    
d = [[0, -1], [0, 1], [1, 0], [-1, 0]]

def dfs(i, j):
    if i == M - 1 and j == N - 1:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0
    
    for a_x, a_y in d:
        dx = i + a_x
        dy = j + a_y
        if 0 <= dx and dx < M and 0 <= dy and dy < N:
            if Map[dx][dy] < Map[i][j]:
                dp[i][j] += dfs(dx, dy)

    return dp[i][j]
    


    
print(dfs(0, 0))
for t in dp:
    print(t)

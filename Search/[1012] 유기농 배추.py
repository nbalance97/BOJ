import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline

T = int(input().rstrip())

cx = [-1, 1, 0, 0]
cy = [0, 0, 1, -1]

for vv in range(T):
    N, M, K = map(int, input().rstrip().split())
    # M행 N열

    C = [[0] * N for _ in range(M)]

    for _ in range(K):
        y, x = map(int, input().rstrip().split())
        C[x][y] = 1

    def dfs(i, j):
        if i < 0 or i >= M or j < 0 or j >= N:
            return
        if C[i][j] == 0:
            return

        C[i][j] = 0

        for t in range(4):
            dfs(i + cx[t], j + cy[t])
            
    block = 0
    for i in range(M):
        for j in range(N):
            if C[i][j] != 0:
                dfs(i, j)
                block += 1

    print(block)


import sys

input = lambda: sys.stdin.readline().rstrip()
T = int(input())

for _ in range(T):
    N = int(input())
    scoreA = list(map(int, input().split()))
    scoreB = list(map(int, input().split()))
    DP = [[0] * 3 for _ in range(N)]
    DP[0][0], DP[0][1], DP[0][2] = 0, scoreA[0], scoreB[0]
    for i in range(1, N):
        DP[i][0] = max(DP[i-1][0], DP[i-1][1], DP[i-1][2])
        DP[i][1] = max(DP[i-1][0], DP[i-1][2]) + scoreA[i]
        DP[i][2] = max(DP[i-1][0], DP[i-1][1]) + scoreB[i]

    print(max(DP[N-1]))

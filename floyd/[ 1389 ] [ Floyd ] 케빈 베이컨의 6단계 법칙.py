import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

INT_MAX = int(10e9)
matrix = [[INT_MAX] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])

kevin = []
for i in range(1, N+1):
    kevin.append([sum(matrix[i][1:]), i])

kevin.sort()
print(kevin[0][1])

import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

matrix = [list(input()) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'N':
            matrix[i][j] = int(10e9)
        else:
            matrix[i][j] = 1

for i in range(N):
    for j in range(N):
        for k in range(N):
            matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])

answer = 0
for i in range(N):
    count = 0
    for j in range(N):
        if j != i and matrix[i][j] <= 2:
            count += 1
    answer = max(answer, count)


print(answer)

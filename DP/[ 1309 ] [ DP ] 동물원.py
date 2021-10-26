import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

matrix = [[0] * 3 for _ in range(N+1)]

for i in range(3):
    matrix[1][i] = 1

for i in range(2, N+1):
    matrix[i][2] = (matrix[i-1][0] + matrix[i-1][1]) % 9901
    matrix[i][1] = (matrix[i-1][0] + matrix[i-1][2]) % 9901
    matrix[i][0] = (matrix[i-1][0] + matrix[i-1][1] + matrix[i-1][2]) % 9901

print(sum(matrix[N]) % 9901)
    

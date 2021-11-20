import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

matrix = [[0] * (M+1) for _ in range(N+1)]

def solve(i, j):
    answer = 0
    if j >= M:
        i, j = i+1, 0 
    if i >= N:
        return 0
    
    if matrix[i-1][j] == 0 or matrix[i][j-1] == 0 or matrix[i-1][j-1] == 0:
        matrix[i][j] = 1
        answer += (1 + solve(i, j+1))
        matrix[i][j] = 0
    answer += solve(i, j+1)

    return answer

print(solve(0, 0) + 1)
        

import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
matrix = [[0] + list(map(int, input().rstrip().split())) for _ in range(N)]
matrix = [[0] * (N+1)] + matrix
answer = 0
def dfs(a, b, c):
    global answer, N
    if a == N and b == N:
        answer = answer + 1
        return
    
    if 1 <= a and a <= N and 1 <= b and b <= N:
        if a+1 <= N and b+1 <= N:
            if matrix[a+1][b+1] != 1 and matrix[a+1][b] != 1 and matrix[a][b+1] != 1:
                dfs(a+1, b+1, 2) # 대각선

        if c == 2:
            if a + 1 <= N and matrix[a+1][b] != 1:
                dfs(a+1, b, 1) # 세로
            if b + 1 <= N and matrix[a][b+1] != 1:
                dfs(a, b+1, 0) # 가로

        if c == 1:
            if a + 1 <= N and matrix[a+1][b] != 1:
                dfs(a+1, b, 1)

        if c == 0:
            if b + 1 <= N and matrix[a][b+1] != 1:
                dfs(a, b+1, 0)
    
dfs(1,2,0)
print(answer)
                
            

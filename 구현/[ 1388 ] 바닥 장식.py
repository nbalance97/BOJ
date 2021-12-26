import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]
count = 0

def process_row(matrix, i, j):
    for k in range(j+1, M):
        if matrix[i][k] == '-':
            matrix[i][k] = '.'
        else:
            break

def process_col(matrix, i, j):
    for k in range(i+1, N):
        if matrix[k][j] == '|':
            matrix[k][j] = '.'
        else:
            break

for i in range(N):
    for j in range(M):
        if matrix[i][j] == '.':
            continue
        if matrix[i][j] == '-':
            matrix[i][j] = '.'
            process_row(matrix, i, j)
        if matrix[i][j] == '|':
            matrix[i][j] = '.'
            process_col(matrix, i, j)
        count += 1
print(count)
            
                

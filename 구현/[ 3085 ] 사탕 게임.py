import sys

input = lambda: sys.stdin.readline().rstrip()
n = int(input())

board = [list(input()) for _ in range(n)]

def get_max_candy(board):
    value = 0
    for i in range(n):
        row_v = 1
        col_v = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                row_v += 1
            else:
                row_v = 1

            if board[j][i] == board[j-1][i]:
                col_v += 1
            else:
                col_v = 1
            
            value = max(value, row_v, col_v)

    return value


answer = 0
for i in range(n):
    for j in range(n):
        if i+1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            answer = max(answer, get_max_candy(board))
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
        if j+1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            answer = max(answer, get_max_candy(board))
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

print(answer)
            
        
    

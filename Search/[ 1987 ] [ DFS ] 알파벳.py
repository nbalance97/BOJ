import sys

input = lambda: sys.stdin.readline().rstrip()
R, C = map(int, input().split())

matrix = [list(input()) for _ in range(R)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = 0

def solve(visited_str, x, y):
    global R, C
    skip = True
    answer = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < R and 0 <= ny and ny < C:
            if matrix[nx][ny] not in visited_str:
                skip = False
                answer = max(answer,
                             1 + solve(visited_str + matrix[nx][ny], nx, ny))

    if skip:
        return 1
    else:
        return answer

print(solve(matrix[0][0], 0, 0))

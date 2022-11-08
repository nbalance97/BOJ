import sys

input = sys.stdin.readline
matrix = [list(map(int, input().split())) for _ in range(5)]
result = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(cnt, i, j, middle_result):
    if cnt == 6:
        result.add(middle_result)
        return

    for t in range(4):
        ni = i + dx[t]
        nj = j + dy[t]
        if 0 <= ni < 5 and 0 <= nj < 5:
            dfs(cnt + 1, ni, nj, middle_result * 10 + matrix[ni][nj])


for i in range(0, 5):
    for j in range(0, 5):
        dfs(0, i, j, 0)

print(len(result))


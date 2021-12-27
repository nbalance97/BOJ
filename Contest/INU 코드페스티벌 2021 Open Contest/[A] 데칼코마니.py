import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
picture = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if picture[i][j] != '.':
            picture[i][M-1-j] = picture[i][j]

for p in picture:
    print("".join(p))

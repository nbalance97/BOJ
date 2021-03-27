import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().rstrip().split())

matrix = []

for _ in range(r):
    matrix.append(list(map(int, input().rstrip().split())))


def bfs(i, j):
    global r, c
    queue = deque()
    queue.append([i, j])
    matrix[i][j] = 0
    count = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            if x + dx[i] >= 0 and x + dx[i] <= r-1 and \
               y + dy[i] >= 0 and y + dy[i] <= c-1:
                if matrix[x + dx[i]][y + dy[i]] == 1:
                    matrix[x + dx[i]][y + dy[i]] = 0
                    count += 1
                    queue.append([x + dx[i], y + dy[i]])

    return count

answer = 0
tot = 0
for i in range(r):
    for j in range(c):
        if matrix[i][j] == 1:
            tot += 1
            answer = max(answer, bfs(i, j))

print(tot)
print(answer)

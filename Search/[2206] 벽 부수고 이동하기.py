import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
matrix = [list(map(int, " ".join(input().rstrip()).split())) for _ in range(N)]


def bfs(matrix, a, b):
    queue = deque()
    queue.append([0, 0, 1, False]) # 현재 x, y, cost, 벽 부셨는지 여부
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    visited_d = [[False] * b for _ in range(a)]  # 벽 부수지 않은 상태에서 방문
    visited = [[False] * b for _ in range(a)] # 벽 부순 상태에서 방문

    visited[0][0] = True
    visited_d[0][0] = True

    while queue:
        cX, cY, cost, isDestroy = queue.popleft()
        if cX == a-1 and cY == b-1:
            return cost
        for i in range(4):
            nX = cX + dx[i]
            nY = cY + dy[i]
            if nX >= 0 and nX < a and nY >= 0 and nY < b:
                if matrix[nX][nY] == 0:
                    if isDestroy and visited_d[nX][nY]:
                        continue
                    if not isDestroy and visited[nX][nY]:
                        continue

                    if isDestroy:
                        visited_d[nX][nY] = True
                    else:
                        visited[nX][nY] = True

                    queue.append([nX, nY, cost+1, isDestroy])

                elif matrix[nX][nY] == 1 and not isDestroy:
                    if visited_d[nX][nY]:
                        continue

                    visited_d[nX][nY] = True
                    queue.append([nX, nY, cost+1, True])

    return -1

print(bfs(matrix, N, M))
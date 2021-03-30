import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

matrix = []

for _ in range(N):
    matrix.append(list(map(int, " ".join(input().rstrip()).split())))

def bfs(matrix, x, y, n, m):
    queue = deque()
    queue.append([x, y, 1])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    matrix[x][y] = 0
    while queue:
        x, y, cost = queue.popleft()
        if x == n-1 and y == m-1:
            return cost
        for i in range(4):
            nextX = x + dx[i]
            nextY = y + dy[i]
            if nextX >= 0 and nextX <= N-1 and nextY >= 0 and nextY <= M-1:
                if matrix[nextX][nextY] == 1:
                    matrix[nextX][nextY] = 0
                    queue.append([nextX, nextY, cost+1])


print(bfs(matrix, 0, 0, N, M))
        
    
    
    

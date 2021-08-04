import sys
import heapq

problem_count = 1
input = sys.stdin.readline
while True:
    n = int(input().rstrip())
    if n == 0:
        break
    matrix = [list(map(int, input().rstrip().split())) for _ in range(n)]
    INT_MAX = int(10e9)
    distance =[[INT_MAX] * n for _ in range(n)]
    heap = []
    distance[0][0] = matrix[0][0]
    heapq.heappush(heap, [matrix[0][0], [0, 0]])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    while heap:
        dist, pos = heapq.heappop(heap)
        if distance[pos[0]][pos[1]] < dist:
            continue
        for i in range(4):
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                if distance[nx][ny] > dist + matrix[nx][ny]:
                    distance[nx][ny] = dist + matrix[nx][ny]
                    heapq.heappush(heap, [dist + matrix[nx][ny], [nx, ny]])
    print("Problem %d: %d"%(problem_count, distance[n-1][n-1]))
    problem_count += 1

import sys

input = lambda : sys.stdin.readline().rstrip()

T = int(input())
lines = [list(map(int, input().split())) for _ in range(T)]
INT_MAX = int(10e9)
graph = [[INT_MAX] * T for _ in range(T)]

for i in range(len(lines)):
    for j in range(i+1, len(lines)):
        if (lines[i][0] <= lines[j][0] and lines[j][0] <= lines[i][1]) or \
        (lines[i][0] <= lines[j][1] and lines[j][1] <= lines[i][1]) or \
        (lines[j][0] <= lines[i][0] and lines[j][1] >= lines[i][1]):
            graph[i][j] = 1
            graph[j][i] = 1

for i in range(T):
    for j in range(T):
        for k in range(T):
            graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k])

Q = int(input())
for _ in range(Q):
    src, dest = map(int, input().split())
    src, dest = src - 1, dest - 1

    if graph[src][dest] == INT_MAX:
        print(-1)
    else:
        print(graph[src][dest])
    

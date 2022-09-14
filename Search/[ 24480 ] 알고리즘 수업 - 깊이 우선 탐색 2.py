import sys
from collections import deque

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    src, dest = map(int, input().split())
    graph[src].append(dest)
    graph[dest].append(src)

for i in range(1, N+1):
    graph[i].sort(reverse=True)

queue = deque([R])
sequence = [0] * (N+1)
seq = 1


def dfs(node):
    global seq

    sequence[node] = seq
    seq += 1

    for next_node in graph[node]:
        if sequence[next_node] == 0:
            dfs(next_node)


dfs(R)
for s in sequence[1:]:
    print(s)

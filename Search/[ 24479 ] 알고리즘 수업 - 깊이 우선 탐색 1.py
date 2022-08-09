import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
n, m, r = map(int, input().split())

graph = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    graph[i].sort()

visited = [False] * (n + 1)
sequence = [0] * (n + 1)

seq = 1


def dfs(current):
    global seq
    visited[current] = True
    sequence[current] = seq
    seq += 1

    for next_node in graph[current]:
        if not visited[next_node]:
            dfs(next_node)


dfs(r)
for i in range(1, n + 1):
    print(sequence[i])

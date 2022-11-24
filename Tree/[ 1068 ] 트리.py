import sys

input = sys.stdin.readline

n = int(input())
parents = list(map(int, input().split()))
delete = int(input())

child = [[] for _ in range(n)]

start = 0
for i, p in enumerate(parents):
    if p == -1:
        start = i
        continue
    if p == delete or i == delete:
        continue

    child[p].append(i)


def dfs(graph, e):
    global delete

    if len(graph[e]) == 0 and e != delete:
        return 1

    leaf_count = 0

    for next_node in graph[e]:
        leaf_count += dfs(graph, next_node)

    return leaf_count


print(dfs(child, start))

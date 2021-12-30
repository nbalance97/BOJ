import sys

sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())

tree = [[] for _ in range(N+1)]
levels = [0] * (N+1)
visited = [False] * (N+1)
visited[1] = True

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def get_child(node, level):
    levels[level] += 1
    for next_node in tree[node]:
        if not visited[next_node]:
            visited[node] = True
            get_child(next_node, level+1)

get_child(1, 0)

answer = sum(map(lambda x:min(x, K), levels))
print(answer)

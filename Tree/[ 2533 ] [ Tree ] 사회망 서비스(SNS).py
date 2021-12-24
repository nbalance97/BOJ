import sys

sys.setrecursionlimit(10**6)

input = lambda: sys.stdin.readline().rstrip()

n = int(input())
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    src, dest = map(int, input().split())
    tree[src].append(dest)
    tree[dest].append(src)

root = 1

dp = [[0, 1] for _ in range(n+1)]
visited = [False] * (n+1)

def solve(node):
    visited[node] = True
    for next_node in tree[node]:
        if not visited[next_node]:
            solve(next_node)
            dp[node][0] += dp[next_node][1]
            dp[node][1] += min(dp[next_node][0], dp[next_node][1])
        

solve(root)
print(min(dp[root]))



import sys


input = sys.stdin.readline
n = int(input().rstrip())
Tree = [[] for _ in range(n+1)]

for _ in range(n):
    temp = list(map(int, input().rstrip().split()))
    select = temp[0]
    for i in range(1, len(temp), 2):
        if temp[i] == -1:
            break
        Tree[select].append([temp[i], temp[i+1]])

visited = [False] * (n + 1)
max_cost = 0
target_node = 0

def dfs(current, current_cost):
    global max_cost, target_node
    for next, cost in Tree[current]:
        if visited[next] == False:
            visited[next] = True
            if current_cost + cost > max_cost:
                max_cost = current_cost + cost
                target_node = next
            dfs(next, current_cost + cost)
            visited[next] = False

visited[1] = True
dfs(1, 0) # 임의의 점 1에서 가장 먼 점을 찾음.

for i in range(n+1):
    visited[i] = False
max_cost = 0

visited[target_node] = True
dfs(target_node, 0) # 가장 먼 점에서 dfs해서 또다른 가장 먼 점으로(트리의 지름)

print(max_cost)
import sys
from collections import deque

input = sys.stdin.readline

K = int(input().rstrip())

def bfs(graph, visited, start):
    visited[start] = 0 # 시작 색은 0
    queue = deque([[start, 0]])
    while queue:
        e, v = queue.popleft() # 현재 색깔
        value = 1 if v == 0 else 0 # 현재 색깔 전환
        for next_edge in graph[e]:
            if visited[next_edge] == -1:
                queue.append([next_edge, value])
                visited[next_edge] = value
            elif visited[next_edge] == v: # 다음 엣지의 색이 현재 색과 같으면 실패
                return False
    return True
    

for _ in range(K):
    V, E = map(int, input().rstrip().split())
    graph = [[] for _ in range(V+1)]
    for __ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [-1] * (V+1)

    answer = True
    for i in range(1, V+1):
        if visited[i] == -1:
            if not bfs(graph, visited, i):
                answer = False
                break

    if answer:
        print("YES")
    else:
        print("NO")

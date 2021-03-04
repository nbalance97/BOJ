import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())

def bfs(N, K):
    visited = [False] * 100001
    queue = deque()

    queue.append([N, 0])
    visited[N] = True
    while queue:
        current, cost = queue.popleft()
        if current == K:
            return cost
        # 저장할때 visited를 True로 바꿔주지 않고 위에서 visited[current] = True로 해주면 queue에 중복 요소가 너무 많이 저장됨 ..
        if current - 1 >= 0 and visited[current - 1] == False:
            visited[current - 1] = True
            queue.append([current - 1, cost+1])
        if current + 1 <= 100000 and visited[current + 1] == False:
            visited[current + 1] = True
            queue.append([current + 1, cost+1])
        if current * 2 <= 100000 and visited[current * 2] == False:
            visited[current * 2] = True
            queue.append([current * 2, cost+1])


print(bfs(N, K))

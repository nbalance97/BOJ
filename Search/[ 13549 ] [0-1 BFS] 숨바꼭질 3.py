from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().rstrip().split())

queue = deque([[N, 0]])
visited = [False] * 100001
visited[N] = True
answer = int(10e9)
while queue:
    next_x, cost = queue.popleft()
    if next_x == K:
        answer = cost
        break

    for step in [next_x * 2, next_x+1, next_x-1]:
        if 0 <= step <= 100000 and not visited[step]:
            if step == next_x * 2:
                queue.appendleft([step, cost])
            else:
                queue.append([step, cost+1])
            visited[step] = True

print(answer)
    

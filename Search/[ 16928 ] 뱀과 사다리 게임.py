import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

table = [-1] * 101

for _ in range(n):
    src, dest = map(int, input().split())
    table[src] = dest

for _ in range(m):
    src, dest = map(int, input().split())
    table[src] = dest

visited = [False] * 101
visited[1] = True

dice = [i for i in range(1, 7)]
queue = deque([[1, 0]])

while queue:
    current_position, movement = queue.popleft()

    if current_position == 100:
        print(movement)
        break

    for d in dice:
        next_position = current_position + d
        if next_position > 100:
            continue

        if table[next_position] != -1:
            next_position = table[next_position]

        if not visited[next_position]:
            visited[next_position] = True
            queue.append([next_position, movement + 1])

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
queue = deque([int(input()) for _ in range(n)])
answer = 0

while True:
    t = 30
    while queue:
        time = queue.popleft()
        target_time = time // 2
        if time % 2 == 1:
            target_time += 1

        if target_time <= t:
            answer += 1
        
        t = max(t - time, 0)
        if t == 0:
            break

    if not queue:
        break

print(answer)

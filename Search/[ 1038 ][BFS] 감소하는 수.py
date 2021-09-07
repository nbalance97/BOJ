import sys
from collections import deque

N = int(input().rstrip())

def bfs(N):
    queue = deque([i for i in range(1, 10)])
    count = 0

    while queue:
        t1 = queue.popleft()
        count += 1
        if count == N:
            return t1
        dest = int(str(t1)[-1])
        for i in range(dest):
            queue.append(int(str(t1) + str(i)))
            
    return -1
            
if N == 0:
    print(0)
else:
    print(bfs(N))

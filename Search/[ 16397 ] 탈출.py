import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, T, G = map(int, input().split())
queue = deque()
queue.append([N, 0])

def get_next_number(i):
    temp = i * 2
    if i == 0 or temp > 99999:
        return [i+1]
    index = 1
    while temp//10 != 0:
        temp //= 10
        index *= 10
    
    return [i+1, i * 2 - index]

visited = set()
visited.add(N)

while queue:
    target, step = queue.popleft()
    if step == T+1:
        print("ANG")
        break
    if target == G:
        print(step)
        break
    for nx in get_next_number(target):
        if nx not in visited:
            queue.append([nx, step+1])
            visited.add(nx)
else:
    print("ANG")

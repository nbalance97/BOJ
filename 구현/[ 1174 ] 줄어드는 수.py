import sys
from collections import deque

input = sys.stdin.readline
n = int(input())

queue = deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

sequence = 0
while queue:
    sequence += 1
    data = queue.popleft()
    if sequence == n:
        print(data)
        break
    target = data % 10
    for i in range(0, target):
        queue.append(data * 10 + i)
else:
    print("-1")

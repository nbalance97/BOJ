import sys
from collections import deque

stack = deque()
n = int(sys.stdin.readline().rstrip())

for _ in range(n):
    p = int(sys.stdin.readline().rstrip())
    while stack:
        if stack[-1] <= p:
            stack.pop()
        else:
            break
    stack.append(p)

print(len(stack))

import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
v = list(input().rstrip())

stack = deque()
val_dict = dict()

for i in range(N):
    val_dict[chr(ord('A')+i)] = int(input().rstrip())

for char in v:
    if char in ['*', '+', '/', '-']:
        p1 = stack.pop()
        p2 = stack.pop()
        result = eval(str(p2) + char + str(p1))
        stack.append(result)
    else:
        stack.append(val_dict[char])

print("%.2f"%(stack.popleft()))

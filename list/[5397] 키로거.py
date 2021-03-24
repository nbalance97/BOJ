import sys
from collections import deque

input = sys.stdin.readline

tcase = int(input().rstrip())


'''
    -----        ------
    left         right
    -----        ------
    left는 append / pop
    right는 appendleft / popleft
    
'''
def getPassword(pattern):
    left = deque()
    right = deque()

    for p in pattern:
        if p == "<":
            if len(left) != 0:
                right.appendleft(left.pop())
        elif p == ">":
            if len(right) != 0:
                left.append(right.popleft())
        elif p == "-":
            if len(left) != 0:
                left.pop()
        else:
            left.append(p)

    return "".join(left) + "".join(right)

for _ in range(tcase):
    pat = input().rstrip()
    print(getPassword(pat))

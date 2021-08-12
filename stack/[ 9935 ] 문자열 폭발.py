import sys
from collections import deque
 
input = sys.stdin.readline
 
string = input().rstrip()
boom = input().rstrip()
 
stack = deque()
for s in string:
    stack.append(s)
    while True:
        if len(stack) < len(boom):
            break
        length_s = len(stack)
        length_b = len(boom)
        flag = False
        for i in range(len(boom)):
            if boom[i] == stack[length_s-length_b+i]:
                pass
            else:
                flag = True
                break
 
        if flag:
            break
        else:
            for i in range(len(boom)):
                stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")

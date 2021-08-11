import sys
from collections import deque

stack = deque()
while True:
    p = sys.stdin.readline().rstrip()

    if p == "고무오리 디버깅 시작":
        continue

    if p == "고무오리 디버깅 끝":
        break

    if p == "문제":
        stack.append(p)
    elif p == "고무오리":
        if len(stack) == 0:
            stack.append('문제')
            stack.append('문제')
        else:
            stack.pop()

if stack:
    print("힝구")
else:
    print("고무오리야 사랑해")


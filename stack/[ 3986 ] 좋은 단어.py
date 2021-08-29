import sys

input = sys.stdin.readline

n = int(input().rstrip())
strlist = [input().rstrip() for _ in range(n)]

answer = 0
for s in strlist:
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    if not stack:
        answer += 1

print(answer)
        

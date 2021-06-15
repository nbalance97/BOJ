import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
P = input().rstrip()

answer = -999999999999

def infixtopostfix(s):
    p = ''
    stack = deque()
    for k in s:
        if ord('0') <= ord(k) and ord(k) <= ord('9'):
            p = p + k
        else:
            if k == '(':
                stack.append('(')
            elif k == ')':
                while True:
                    r = stack.pop()
                    if r == '(':
                        break
                    else:
                        p = p + r
            else:
                if len(stack) != 0 and stack[-1] != '(':
                    r = stack.pop()
                    p = p + r
                    stack.append(k)
                else:
                    stack.append(k)
    while stack:
        r = stack.pop()
        p = p + r

    return p

def calculate(fix):
    stack = deque()
    for t in fix:
        if ord('0') <= ord(t) and ord(t) <= ord('9'):
            stack.append(int(t))
        else:
            t2 = stack.pop()
            t1 = stack.pop()
            temp = 0
            if t == '+':
                temp = t1 + t2
            elif t == '-':
                temp = t1 - t2
            elif t == '*':
                temp = t1 * t2
            stack.append(temp)

    return stack.pop()

def dfs(N, flg, idx):
    global answer
    if idx == len(N):
        answer = max(answer, calculate(infixtopostfix(N)))
        return
    if ord('0') <= ord(N[idx]) and ord(N[idx]) <= ord('9'):
        if flg == False:
            if idx == len(N)-1:
                dfs(N, False, idx+1)
            else:
                dfs(N[:idx] + '(' + N[idx:], True, idx+2)
                dfs(N, False, idx+1)
        else:
            dfs(N[:idx+1] + ')' + N[idx+1:], False, idx+1)
    else:
        dfs(N, flg, idx+1)
dfs(P, False, 0)

print(answer)

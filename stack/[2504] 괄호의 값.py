import sys
from collections import deque


gh = deque()

st = sys.stdin.readline().rstrip()
fail = False

for s in st:
    if s == "(" or s == "[": # 열린 괄호는 그냥 넣어줌
        gh.appendleft(s)
        
    elif s == "]": 
        num = []
        if len(gh) == 0: # 닫힌 괄호가 보였는데 스택에 아무것도 없으면 fail
            fail = True
            break
        
        while True: # 괄호 사이에 있는 숫자들을 모두 구함
            if len(gh) == 0: # 이 과정에서 스택이 비면 오류
                fail = True
                break
            nx = gh.popleft()
            if nx == "[": # 열린괄호 보이면 중지
                break
            elif nx == "(": # 다른 열린괄호 보이면 문제 있음
                fail = True
                break
            else:
                num.append(nx)

        if len(num) == 0: # 괄호 사이에 숫자가 없는 경우는 3, 있는 경우는 합계 * 3
            gh.appendleft(3)
        else:
            gh.appendleft(sum(num) * 3)


    elif s == ")":
        num = []
        if len(gh) == 0:
            fail = True
            break
        
        while True:
            if len(gh) == 0:
                fail = True
                break
            nx = gh.popleft()
            if nx == "(":
                break
            elif nx == "[":
                fail = True
                break
            else:
                num.append(nx)

        if len(num) == 0: # 괄호 사이에 숫자가 없는 경우는 2, 있는 경우는 합계 * 2
            gh.appendleft(2)
        else:
            gh.appendleft(sum(num) * 2)           
    else: # 괄호 이외에 다른 문자열 존재 시 fail
        fail = True

    if fail: 
        break

if "[" in gh or "(" in gh or fail: # 만약 스택에 괄호가 남아있거나 fail인 경우는 0 출력
    print(0)
else:
    print(sum(gh))

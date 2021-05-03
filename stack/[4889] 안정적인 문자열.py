import sys
from collections import deque

input = sys.stdin.readline

def get_answer(strs):
    answer = 0
    queue = deque()
    for x, char in enumerate(strs):
        if char == '{':
            if len(strs)-x <= len(queue): # {가 나왔을 때 남아있는 문자열보다 queue에 들어있는게 많으면 무조건 빼야함
                queue.pop()
                answer += 1
            else:
                queue.append(char)
        elif char == "}":
            if len(queue) == 0: # }가 나왔을 때 stack이 비어있다면 {로 바꾸고 채워 넣어주어야 함.
                queue.append("{")
                answer += 1
            else:
                queue.pop()
    return answer

idx = 0
while True:
    idx = idx + 1
    test = input().rstrip()
    if test[0] == "-":
        break
    answer = get_answer(test)
    print(str(idx)+". "+str(answer))

# stack 문제 풀때는 문제를 중간중간 어느정도 줄여야 하는게 핵심인듯.

import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
buildings = [int(input().rstrip()) for _ in range(n)]

stack = deque()
answer = 0
for i in range(n):
    # 자기 기준 좌측 건물들을 자기보다 큰 건물만 남기고 없앰.
    # 어차피 다음 건물은 현재 왼쪽의 건물들이 자신보다 작다면
    # 자신때문에 오른쪽 건물을 볼 수 없음
    while stack and buildings[stack[-1]] <= buildings[i]:
        stack.pop()
    answer = answer + len(stack)
    stack.append(i) # 자기를 stack에 넣음

    
print(answer)

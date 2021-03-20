import sys
from collections import deque

input = sys.stdin.readline

edit = input().rstrip()
N = int(input().rstrip())

left = deque()
right = deque()

# 이런 유형의 문제는 큐 두개 두고 푸는게 제일 좋음.
# 그냥 가운데 pop해버리면 O(n) 돌게 되어 문제 생김
# appendleft, append, popleft, pop같은 경우 O(1)이므로 훨씬 빠른 점 이용

for e in edit:
    left.append(e)
    
for i in range(N):
    cmd = list(input().rstrip().split())
    if cmd[0] == 'L' and len(left) != 0:
        right.appendleft(left.pop())
            
    if cmd[0] == 'D' and len(right) != 0:
        left.append(right.popleft())

    if cmd[0] == 'B' and len(left) != 0:
        left.pop()

    if cmd[0] == 'P':
        left.append(cmd[1])
        
print("".join(left)+"".join(right))

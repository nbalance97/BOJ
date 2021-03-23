import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
answer = [0] * (N+1)
L = [0] + list(map(int, input().rstrip().split()))

queue = deque()
p = len(L)-1
queue.appendleft([L[p], p]) # 마지막 건물의 높이와 번호

for i in range(p-1, 0, -1):
    while True:
        # 현재 탑 기준으로 스택 내에 작은 크기의 탑이 있다면
        # 정답 명시해주고 스택에서 빼내줌.
        # 여기서 참고해야 할 사항은, 스택 내에는 오름차순으로 값이 쌓일 것이라는
        # 점임.
        if queue[0][0] <= L[i]: 
            _, pos = queue.popleft() 
            answer[pos] = i
            if len(queue) == 0:
                break
        else:
            break
            
    # 현재 탑을 스택에 저장
    queue.appendleft([L[i], i]) 

print(" ".join(map(str, answer[1:])))
            
        
        

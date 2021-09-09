from collections import deque

N = int(input())
temp = list(map(int, input().split()))

balloon = [[i+1, boom] for i, boom in enumerate(temp)]
balloon = deque(balloon)

start = 0

boom = []
while True:
    idx, step = balloon.popleft()
    boom.append(idx)

    if not balloon:
        break
    
    if step > 0:
        step = abs(step)
        for i in range(step-1):
            balloon.append(balloon.popleft())
    else:
        step = abs(step)
        for i in range(step):
            balloon.appendleft(balloon.pop())
    
print(*boom)

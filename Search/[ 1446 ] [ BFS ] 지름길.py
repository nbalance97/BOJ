import sys
from collections import defaultdict, deque
 
input = lambda : sys.stdin.readline().rstrip()
 
N, D = map(int, input().split())
temp = defaultdict(lambda:int(10e9))
 
for _ in range(N):
    s, e, d = map(int, input().split())
    temp[(s, e)] = min(temp[(s, e)], d)
 
shortcut = defaultdict(lambda:[])
for (s, e), d in temp.items():
    shortcut[s].append([e, d])
 
queue = deque()
queue.append([0, 0])
 
answer = int(10e9)
while queue:
    current, movement = queue.popleft()
    if current > D:
        continue
    if current == D:
        answer = min(answer, movement)
        continue
    if shortcut.get(current) != None:
        for e, d in shortcut[current]:
            queue.append([e, movement + d])    
    queue.append([current+1, movement+1])
    
print(answer)

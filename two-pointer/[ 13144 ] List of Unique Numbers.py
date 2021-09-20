import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

n = int(input())
sequence = list(map(int, input().split()))

dp = [0] * len(sequence)
queue = deque()
current = set()
for i in range(len(sequence)):
    if sequence[i] in current:
        while queue:
            pos, value = queue.popleft()
            current.remove(value)
            if value == sequence[i]:
                break
    queue.append([i, sequence[i]])
    current.add(sequence[i])

    dp[i] = len(current)
    
print(sum(dp))
            

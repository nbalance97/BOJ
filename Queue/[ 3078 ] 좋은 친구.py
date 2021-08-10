import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
len_count = {i:0 for i in range(2, 21)}

queue = deque()
answer = 0
for i in range(N):
    friend = input().rstrip()
    if i > K:
        t = queue.popleft()
        len_count[len(t)] -= 1
    answer += len_count[len(friend)]
    queue.append(friend)
    len_count[len(friend)] += 1

print(answer)

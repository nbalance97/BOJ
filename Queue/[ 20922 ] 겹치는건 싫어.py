import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))
sequence = set()
dup_count = {i:0 for i in range(1, 100001)}
answer = 0

queue = deque()
for number in numbers:
    queue.append(number)
    dup_count[number] += 1
    # number에서 중복 문제 걸림
    if dup_count[number] > K:
        # number가 나올때까지 queue에서 싹 빼주어야 함.
        while queue:
            temp = queue.popleft()
            dup_count[temp] -= 1
            if temp == number:
                break
    answer = max(answer, len(queue))

print(answer)


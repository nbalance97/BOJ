import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

sequence = list(map(int, input().split()))
numbers = defaultdict(lambda: set())
for i in range(len(sequence)):
    numbers[sequence[i]].add(i)

answer = 0

if len(sequence) <= 2:
    print(0)
    sys.exit(0)

for i in range(N):
    for j in range(i+1, N):
        temp = sequence[i] + sequence[j]
        candidate = []
        for item in numbers[temp]:
            if item != i and item != j:
                candidate.append(item)

        for item in candidate:
            numbers[temp].remove(item)
            answer += 1
            

print(answer)


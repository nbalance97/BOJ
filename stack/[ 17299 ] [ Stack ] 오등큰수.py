import sys
from collections import Counter

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
sequence = list(map(int, input().split()))
answer = [-1] * N
stack = []
alpha = Counter(sequence)
for i in range(len(sequence)):
    while stack and alpha[sequence[stack[-1]]] < alpha[sequence[i]]:
        q = stack.pop()
        answer[q] = sequence[i]
    stack.append(i)
print(*answer)
        

import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()


alpha = defaultdict(lambda: 0)
N = int(input())
for _ in range(N):
    word = input()
    size = len(word)
    for idx, ch in enumerate(word):
        alpha[ch] += (10 ** (size-1-idx))

temp = sorted(alpha.values(), reverse=True)
pos = 0
answer = 0
for i in range(9, 0, -1):
    answer += temp[pos] * i
    pos += 1
    if pos == len(temp):
        break

print(answer)
    

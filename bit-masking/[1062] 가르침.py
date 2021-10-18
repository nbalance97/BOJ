import sys
from itertools import combinations

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
words = [0] * N

for i in range(N):
    word = list(input())[4:-4]
    for ch in word:
        words[i] |= (1 << ord(ch) - ord('a'))
        
answer = 0
if K < 5:
    pass
else:
    alpha = 'bdefghjklmopqrsuvwxyz'
    base = ['a', 'n', 't', 'i', 'c']
    append_case = list(combinations(list(alpha), K-5))
    for case in append_case:
        make_bit = 0
        for ch in base:
            make_bit |= (1 << ord(ch) - ord('a'))
        for ch in case:
            make_bit |= (1 << ord(ch) - ord('a'))

        count = 0
        for i in range(len(words)):
            if words[i] & make_bit == words[i]:
                count += 1
        

        answer = max(answer, count)
        
print(answer)        
    

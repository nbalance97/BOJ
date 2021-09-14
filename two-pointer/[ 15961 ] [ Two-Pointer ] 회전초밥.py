import sys
from collections import defaultdict

input = lambda :sys.stdin.readline().rstrip()

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
case = set()
case_count = defaultdict(int)
answer = 0

left = 0
right = k-1

for i in range(k):
    case.add(sushi[i])
    case_count[sushi[i]] += 1

total_case = len(case)+1 if c not in case else len(case)
answer = max(answer, total_case)


for i in range(N):
    case_count[sushi[left]] -= 1
    if case_count[sushi[left]] == 0: case.remove(sushi[left])
    left = (left + 1) % N
    
    right = (right + 1) % N
    if sushi[right] not in case: case.add(sushi[right])
    case_count[sushi[right]] += 1
    
    total_case = len(case)+1 if c not in case else len(case)
    answer = max(answer, total_case)
        
print(answer)

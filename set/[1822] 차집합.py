import sys


nA, nB = map(int,sys.stdin.readline().rstrip().split())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

A.sort()
B = set(B)
answer = []

for a in A:
    if a not in B:
        answer.append(a)
        
print(len(answer))
if answer:
    print(*answer)

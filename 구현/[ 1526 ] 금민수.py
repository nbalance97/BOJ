import sys
from bisect import bisect_left

p = []

def add(n):
    if n > 1000000:
        return
    if n != 0:
        p.append(n)
    add(n * 10 + 4)
    add(n * 10 + 7)

add(0)
p.sort()

N = int(sys.stdin.readline().rstrip())
for i in range(len(p)):
    if p[i] == N:
        print(p[i])
        break
    if p[i] > N:
        print(p[i-1])
        break
else:
    print(p[-1])
        

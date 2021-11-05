import sys
import heapq

input = lambda: sys.stdin.readline().rstrip()
l = list(map(int, input().split()))

for e in range(1, len(l)):
    if l[e] < l[e-1]:
        print('Bad')
        break
else:
    print('Good')
    

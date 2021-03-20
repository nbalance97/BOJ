import sys
import bisect

input = sys.stdin.readline
N = int(input().rstrip())
card = list(map(int, input().rstrip().split()))
card.sort()

M = int(input().rstrip())
k = list(map(int,input().rstrip().split()))
for t in k:
    p = bisect.bisect_left(card, t) # 이진 탐색해서 왼쪽에서 삽입할 위치 찾음
    if p == N:
        print(0, end=" ")
        continue
    
    if card[p] == t:
        print(1, end=" ")
    else:
        print(0, end=" ")

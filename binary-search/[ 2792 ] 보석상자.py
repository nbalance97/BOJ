import sys

input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
color = [int(input()) for _ in range(M)]

left, right = 1, 10**10

answer = 0
while left <= right:
    mid = (left + right) // 2
    count = 0
    for c in color:
        count += (c // mid)
        if c % mid != 0:
            count += 1
    

    if count <= N:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
        

import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
liquids = list(map(int, input().split()))
liquids.sort()

answer = int(10e9)
a, b, c = 0, 0, 0
for std in range(N-2):
    left = std+1
    right = N-1
    end = False
    while left < right:
        temp = liquids[left] + liquids[right] + liquids[std]
        if abs(temp) < abs(answer):
            answer = abs(temp)
            a, b, c = liquids[std], liquids[left], liquids[right]

        if temp == 0:
            end = True
            break
        
        if temp < 0:
            left += 1
        else:
            right -= 1

    if end:
        break

print(a, b, c)

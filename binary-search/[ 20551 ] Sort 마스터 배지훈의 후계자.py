import sys

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
array = [int(input()) for _ in range(N)]
array.sort()

def bisect_left(array, value):
    left = 0
    right = len(array)-1
    pos = -1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == value:
            pos = mid

        if array[mid] >= value:
            right = mid-1
        else:
            left = mid+1

    return pos

for _ in range(M):
    pos = int(input())
    print(bisect_left(array, pos))

import sys

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())

types = {}

def bisect(value, arr):
    left = 0
    right = len(arr)-1
    target = 0
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= value:
            target = mid
            right = mid - 1
        else:
            left = mid + 1

    return target

values = []
for _ in range(N):
    name, value = input().split()
    value = int(value)
    if types.get(value) == None:
        types[value] = name
        values.append(int(value))

values.sort()
for _ in range(M):
    value = int(input())
    pos = bisect(value, values)
    print(types[values[pos]])
    
    
 

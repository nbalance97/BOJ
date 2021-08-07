import sys

input = sys.stdin.readline
N, M, L = map(int, input().rstrip().split())
stations = list(map(int, input().rstrip().split()))
stations = [0] + stations + [L]
stations.sort()

left = 0
right = L
answer = 0
while left <= right:
    mid = (left + right) // 2

    # simulate
    add_count = 0
    for i in range(1, len(stations)):
        dist = stations[i] - stations[i-1]
        if dist > mid:
            add_count += (dist // mid)
            if dist % mid == 0:
                add_count -= 1
    if add_count > M:
        left = mid + 1
    else:
        answer = mid
        right = mid - 1

print(answer)

        
    
        

import sys

input = sys.stdin.readline

N = int(input().rstrip())
lists = list(map(int, input().rstrip().split()))
M = int(input().rstrip())

left = 0
right = max(lists)
answer = 0
while left <= right:
    mid = (left + right) // 2
    total = M
    succeed = True
    for k in lists:
        if (total < mid and k >= mid) or (
            total < k and k < mid ):
            succeed = False
        if succeed:
            if k < mid: # 현재 값보다 리스트 요소가 작으면 k만큼 빼줌
                total -= k
            else: # 현재 값보다 리스트 요소가 크면 현재 값만큼 빼줌
                total -= mid
        else:
            break

    if succeed:
        answer = mid
        left = mid+1
    else:
        right = mid-1

print(answer)

import sys

input = lambda : sys.stdin.readline().rstrip()
N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]

left = 0
right = (1000000000 * int(10e9)) + 1
answer = 0
while left <= right:
    mid = (left + right) // 2

    # 중간값일때, 심사받는 사람의 수 구함
    evaluated_people_count = 0
    for time in T:
        evaluated_people_count += (mid // time)

    # 심사받는 사람의 수가 M보다 작으면 시간을 늘려야 하므로 오른쪽 구간
    # M보다 크거나 같으면 시간을 줄여야 하므로 왼쪽 구간
    if evaluated_people_count >= M:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)
    

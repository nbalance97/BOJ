import sys

input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    left,right = 1, 100000
    movement_count = 0
    
    # 이분 탐색으로 몇번째 이동에서 N-1번째 이동이 걸리는지 탐색
    while left <= right:
        mid = (left + right) // 2
        movement = int(((K + K + (mid-1) * K) / 2 ) * mid)
        if movement > N-1:
            right = mid-1
            movement_count = mid
        else:
            left = mid+1
            
    way = ''
    if movement_count % 2 == 1:
        way = 'R'
    else:
        way = 'L'
    
    # 이전 단계까지의 이동 횟수를 빼주어서 남은 이동 횟수 저장(remainder)
    before_movement = int(((K + K + (movement_count-2) * K) / 2 ) * (movement_count-1))
    remainder = (N-1) - before_movement
    
    # 이전 단계까지의 이동 결과 최종적으로 위치하고 있는 x좌표 구함
    step = (movement_count-1) // 2
    start = K * step
    if (movement_count-1) % 2 == 1:
        start += K
    else:
        start *= -1
    
    # 남아있는 이동 횟수 이동
    if way == 'R':
        start += remainder
    else:
        start -= remainder
    
    print(start, way)

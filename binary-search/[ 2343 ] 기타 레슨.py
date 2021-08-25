import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lessons = list(map(int, input().rstrip().split()))

left = max(lessons)
right = 100000 * 10000

answer = max(lessons)

while left <= right:
    # middle : blueray의 길이
    middle = (left + right) // 2

    blueray = 1
    current = middle

    # blueray의 길이가 middle일때 몇개 나오는지 
    for lesson in lessons:
        if current - lesson < 0:
            blueray += 1
            current = middle - lesson
        else:
            current = current - lesson
            
    # blueray의 길이가 M보다 작다면 정답 저장 후 blueray를 줄여야 함
    # blueray의 길이가 M보다 크다면 blueray를 늘려야 함
    if blueray <= M:
        answer = middle
        right = middle - 1
    elif blueray > M:
        left = middle + 1

print(answer)

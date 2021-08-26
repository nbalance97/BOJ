import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

sequence = list(map(int, input().rstrip().split()))
left = 0
right = 1
sumation = sequence[left]
answer = 0
while left <= right:
    if sumation == M:
        answer += 1

    # 합계가 M보다 크다면 왼쪽에서 하나 끌고와서 빼준다.
    if sumation > M:
        sumation -= sequence[left]
        left += 1
    # 합계가 M보다 작거나 같다면 오른쪽으로 한칸 늘려준다.
    elif sumation <= M:
        if right == N:
            break
        sumation += sequence[right]
        right += 1

print(answer)
        
        

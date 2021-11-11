import sys

input = lambda: sys.stdin.readline().rstrip()
N, K, D = map(int, input().split())

left = 1
right = 1000000
rule = [list(map(int, input().split())) for _ in range(K)]

def check_answer(box_num):
    total_count = 0
    for r in rule:
        start, end, gap = r
        if start > box_num:
            continue
        last = min(end, box_num)
        current_count = (last - start) // gap
        current_count += 1
        total_count += current_count
    return total_count

answer = 0
while left <= right:
    mid = (left + right) // 2
    total = check_answer(mid)
    if total >= D:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)

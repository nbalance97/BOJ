import sys

input = lambda : sys.stdin.readline().rstrip()
M, N = map(int, input().split())
snacks = list(map(int, input().split()))

def test(snacks, target, target_people_count):
    people_count = 0

    if target == 0:
        return False
    
    for snack in snacks:
        people_count += (snack // target)

    if people_count >= target_people_count:
        return True
    else:
        return False

left, right = 0, int(10e9)+1

answer = 0
while left <= right:
    mid = (left + right) // 2
    if test(snacks, mid, M):
        answer = mid
        left = mid+1
    else:
        right = mid-1

print(answer)

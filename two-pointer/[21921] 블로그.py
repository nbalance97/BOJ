import sys

input = lambda : sys.stdin.readline().rstrip()
N, X = map(int, input().split())
log = list(map(int, input().split()))

max_visitor = 0
max_visitor_cnt = 0

visitor = sum(log[:X])
left = 0
right = X-1

while right < N:
    if max_visitor < visitor:
        max_visitor = visitor
        max_visitor_cnt = 1
    elif max_visitor == visitor:
        max_visitor_cnt += 1

    if right == N-1:
        break

    visitor -= log[left]
    left += 1
    right += 1
    visitor += log[right]

if max_visitor == 0:
    print("SAD")
else:
    print(max_visitor)
    print(max_visitor_cnt)

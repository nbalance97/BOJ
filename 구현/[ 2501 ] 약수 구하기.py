import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())

answer_count = 0
for i in range(1, N+1):
    if N % i == 0:
        answer_count += 1
    if answer_count == K:
        print(i)
        break
else:
    print(0)

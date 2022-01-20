import sys

input = lambda: sys.stdin.readline().rstrip()
T = int(input())

for _ in range(T):
    N = int(input())
    applicants = [list(map(int, input().split())) for _ in range(N)]
    applicants.sort()
    max_r2 = 999999
    answer = 0
    for _, r2 in applicants:
        if r2 < max_r2:
            max_r2 = r2
            answer += 1

    print(answer)

import sys
from itertools import permutations

input = sys.stdin.readline
N = int(input().rstrip())
W = [list(map(int, input().rstrip().split())) for _ in range(N)]

total_case = list(permutations([i for i in range(N)], N))

def check_case(W, case):
    case = case + (case[0], )
    cost = 0
    for i in range(1, len(case)):
        if W[case[i]][case[i-1]] == 0:
            return int(10e9)
        cost += W[case[i]][case[i-1]]

    return cost

answer = int(10e9)
for case in total_case:
    answer = min(answer, check_case(W, case))

print(answer)

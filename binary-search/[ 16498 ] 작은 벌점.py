import sys
from bisect import bisect_left

input = sys.stdin.readline

a_size, b_size, c_size = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()
answer = sys.maxsize
for i in A:
    for j in B:
        found_val = bisect_left(C, max(i, j))
        found_another = bisect_left(C, min(i, j))
        if found_val == len(C) or C[found_val] != max(i, j):
            found_val = found_val - 1 if found_val != 0 else found_val
        if found_another == len(C):
            found_another = found_another - 1

        answer = min(answer, abs(max(i, j, C[found_val]) - min(i, j, C[found_val])))
        answer = min(answer, abs(max(i, j, C[found_another]) - min(i, j, C[found_another])))


print(answer)

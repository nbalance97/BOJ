import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())

a, b, c, d = [], [], [], []
for _ in range(n):
    a_data, b_data, c_data, d_data = map(int, input().split())
    a.append(a_data)
    b.append(b_data)
    c.append(c_data)
    d.append(d_data)

cd_case = defaultdict(int)

for i in range(n):
    for j in range(n):
        cd_case[c[i] + d[j]] += 1

answer = 0

for i in range(n):
    for j in range(n):
        k = a[i] + b[j]
        if -k in cd_case.keys():
            answer += cd_case[-k]



print(answer)


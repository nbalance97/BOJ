import sys


temp = [0] + []
for i in range(1, 51):
    for j in range(i):
        temp.append(i)

a, b = map(int, sys.stdin.readline().rstrip().split())

s = 0
for i in range(a, b+1):
    s += temp[i]

print(s)

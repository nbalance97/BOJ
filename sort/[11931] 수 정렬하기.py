import sys

input = sys.stdin.readline

num = [0] * 1000001

p = int(input())

answer = []
for _ in range(p):
    idx = int(input())
    answer.append(idx)

answer.sort()
answer = answer[::-1]

for _ in answer:
    print(_)

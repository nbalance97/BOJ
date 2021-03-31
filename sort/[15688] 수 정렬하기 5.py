import sys

input = sys.stdin.readline

num = [0] * 1000001

p = int(input())

answer = []
for _ in range(p):
    idx = int(input())
    answer.append(idx)

# python의 sort 함수는 O(n log n)
answer.sort()
for _ in answer:
    print(_)

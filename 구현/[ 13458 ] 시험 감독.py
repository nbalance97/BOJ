import sys

input = sys.stdin.readline
N = int(input().rstrip())
exam = list(map(int, input().rstrip().split()))
B, C = map(int, input().rstrip().split())

answer = 0

for i in range(len(exam)):
    exam[i] -= B
    answer += 1

for i in range(len(exam)):
    if exam[i] <= 0:
        continue
    answer += (exam[i] // C)
    if exam[i] % C != 0:
        answer += 1

print(answer)

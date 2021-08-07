import sys

input = sys.stdin.readline
N = int(input().rstrip())

numbers = [int(input().rstrip()) for _ in range(N)]
number_set = set(numbers)

answer = 0

for i in range(N-1, -1, -1):
    for j in range(i, -1, -1):
        for k in range(j, -1, -1):
            if numbers[i] + numbers[j] + numbers[k] in number_set:
                answer = max(answer, numbers[i] + numbers[j] + numbers[k])

print(answer)

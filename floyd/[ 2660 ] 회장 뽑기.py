import sys
import copy

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
INT_MAX = int(10e9)

matrix = [[INT_MAX] * (n+1) for _ in range(n+1)] 

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    matrix[a][b] = 1
    matrix[b][a] = 1

for i in range(1, n+1):
    matrix[i][i] = 0
    matrix[i][0] = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])

scores = [max(matrix[i]) for i in range(1, n+1)]
score = min(scores)
people = []
for i in range(len(scores)):
    if scores[i] == score:
        people.append(i+1)

print(score, len(people))
print(*people)

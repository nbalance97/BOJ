import sys

input = sys.stdin.readline

n = int(input())

executor = []
undo = [0] * n

for i in range(n):
    cmd, x, time = input().rstrip().split(" ")
    executor.append([cmd, x, time])

for i in range(n-1, -1, -1):
    if executor[i][0] == 'undo' and undo[i] % 2 == 0:
        lower_bound = int(executor[i][2]) - int(executor[i][1])
        for j in range(i - 1, -1, -1):
            if int(executor[j][2]) >= lower_bound:
                undo[j] += 1
            else:
                break

answer = ""
for i in range(n):
    if executor[i][0] == 'type' and undo[i] % 2 == 0:
        answer += executor[i][1]

print(answer)





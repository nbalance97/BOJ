import sys
import heapq


sequence = [(i, j, k)
            for i in range(1, 10)
            for j in range(1, 10)
            for k in range(1, 10)
            if i != j and j != k and i != k]

n = int(sys.stdin.readline().rstrip())
num_list = []
strike_list = []
ball_list = []
for _ in range(n):
    num, strike, ball = map(int, sys.stdin.readline().rstrip().split())
    num_list.append(list(map(int, list(str(num)))))
    strike_list.append(strike)
    ball_list.append(ball)

answer = 0

for x, y, z in sequence:
    for i in range(n):
        strike_count = 0
        ball_count = 0
        if num_list[i][0] == x:
            strike_count += 1
        else:
            if num_list[i][0] == y or num_list[i][0] == z:
                ball_count += 1
                
        if num_list[i][1] == y:
            strike_count += 1
        else:
            if num_list[i][1] == x or num_list[i][1] == z:
                ball_count += 1
                
        if num_list[i][2] == z:
            strike_count += 1
        else:
            if num_list[i][2] == y or num_list[i][2] == x:
                ball_count += 1

        if strike_count != strike_list[i] or ball_count != ball_list[i]:
            break
    else:
        answer += 1

print(answer)

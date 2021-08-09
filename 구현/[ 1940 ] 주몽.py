import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))
numbers.sort()
set_numbers = set(numbers)
max_number = numbers[-1]

answer = 0
for number in numbers:
    if number > M // 2:
        break
    elif number == M // 2:
        if M % 2 == 0: # 고유번호이므로 중복 x
            break
        else:
            if M - number in set_numbers:
                answer += 1
    else:
        if M-number in set_numbers:
            answer += 1
        
print(answer)

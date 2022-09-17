import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
problems = set(list(map(int, input().split())))
btn_count = sys.maxsize

for make in range(0, 1000000):
    if make == 100:
        btn_count = min(btn_count, abs(100 - n))
        continue

    temp_numbers = list(str(make))
    numbers = set(map(int, temp_numbers))
    can = True

    for number in numbers:
        if number in problems:
            break
    else:
        btn_count = min(btn_count, len(temp_numbers) + abs(make - n))

print(btn_count)

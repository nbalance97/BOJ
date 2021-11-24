import sys

input = lambda: sys.stdin.readline().rstrip()
before = list(map(int, input().split()))
before = 360 * before[0] + 30 * before[1] + before[2]
after = list(map(int, input().split()))
after = 360 * after[0] + 30 * after[1] + after[2]

A = 15
temp = after - before
v_year = 0
year = 0
tic_count = 0
while True:
    temp -= 360
    year += 1
    if temp < 0:
        break
    v_year += A
    tic_count += 1
    if tic_count == 2:
        tic_count = 0
        A += 1

v_month = min((after - before) // 30, 36)
print(v_year, v_month)
print(after-before,end="days")


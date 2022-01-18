import sys

input = lambda: sys.stdin.readline().rstrip()
hour, minute, second = map(int, input().split())
D = int(input())

for _ in range(D):
    second += 1
    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        hour += 1
        minute = 0
    if hour == 24:
        hour = 0

print(hour, minute, second)

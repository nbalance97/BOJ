import sys

input = sys.stdin.readline

n, t = map(int, input().split())

buses = [list(map(int, input().split())) for _ in range(n)]

bus_arrive = []

for s, l, c in buses:
    for j in range(c):
        bus_arrive.append(s + (l * j))

bus_arrive.sort()

left = 0
right = 10000000
answer = -1

while left <= right:
    mid = (left + right) // 2
    for bus in bus_arrive:
        if t <= bus <= t + mid:
            break
    else:
        left = mid + 1
        continue

    right = mid - 1
    answer = mid


print(answer)

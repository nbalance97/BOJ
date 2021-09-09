
N = int(input())
ph = list(map(int, input().split()))

left = 0
right = N-1

min_ph = int(10e9)
value1, value2 = 0, 0

while left < right:
    if abs(ph[left] + ph[right]) <= min_ph:
        min_ph = abs(ph[left] + ph[right])
        value1 = ph[left]
        value2 = ph[right]

    if ph[left] + ph[right] > 0:
        right -= 1
    else:
        left += 1

print(value1, value2)

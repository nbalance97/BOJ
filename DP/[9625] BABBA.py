import sys
n = int(sys.stdin.readline().rstrip())

dp_a = [0] * (n+1)
dp_b = [0] * (n+1)

dp_a[0] = 1
dp_b[0] = 0
dp_a[1] = 0
dp_b[1] = 1

for i in range(2, n+1):
    dp_a[i] = dp_a[i-1] + dp_a[i-2]
    dp_b[i] = dp_b[i-1] + dp_b[i-2]

print(dp_a[n], dp_b[n])


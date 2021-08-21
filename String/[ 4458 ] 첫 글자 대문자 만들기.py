import sys

input = sys.stdin.readline
n = int(input().rstrip())


for _ in range(n):
    k = input().rstrip('\n')
    if len(k) > 0:
        upper = k[0].upper()
        k = upper + k[1:]
        print(k)
    else:
        print('')

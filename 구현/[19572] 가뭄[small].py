import sys

input = lambda: sys.stdin.readline().rstrip()

d1,d2,d3 = map(int, input().split())

a = (d1 + d2 - d3) / 2
b = (d1 + d3 - d2) / 2
c = (d2 + d3 - d1) / 2

a,b,c = round(a, 1), round(b, 1), round(c, 1)

if a <= 0 or b <= 0 or c <= 0:
    print(-1)
else:
    print(1)
    print("%.1f %.1f %.1f"%(a, b, c))

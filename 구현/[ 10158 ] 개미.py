import sys

input = lambda: sys.stdin.readline().rstrip()

# 결국 x축, y축으로 상하운동 한다고 보면 된다.

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

xm = t % (w * 2)
ym = t % (h * 2)


add = 1
for _ in range(xm):
    p += add
    if p == w or p == 0:
        add *= -1

add = 1
for _ in range(ym):
    q += add
    if q == h or q == 0:
        add *= -1

print(p, q)

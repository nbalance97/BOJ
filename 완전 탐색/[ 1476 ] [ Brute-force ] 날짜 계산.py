import sys

E, S, M = map(int, sys.stdin.readline().rstrip().split())

e, s, m = 1, 1, 1
year = 1
while True:
    if e == E and s == S and m == M:
        print(year)
        break
    year += 1
    e = (e + 1) % 16
    e = 1 if e == 0 else e
    s = (s + 1) % 29
    s = 1 if s == 0 else s
    m = (m + 1) % 20
    m = 1 if m == 0 else m


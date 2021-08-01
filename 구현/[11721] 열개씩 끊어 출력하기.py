import sys

p = sys.stdin.readline().rstrip()
while len(p) != 0:
    print(p[:10])
    p = p[10:]

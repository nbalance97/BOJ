import sys

tmp = list(map(int, sys.stdin.readline().rstrip().split()))
tmp.sort()
print(" ".join(list(map(str, tmp))))

import sys

input = lambda: sys.stdin.readline().rstrip('\n')
t = input()

if 'D2' in t or 'd2' in t:
    print('D2')
else:
    print('unrated')

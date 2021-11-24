import sys

input = lambda: sys.stdin.readline().rstrip()
s = input()

if len(s) >= 5 and s[-5:] == 'driip':
    print('cute')
else:
    print('not cute')

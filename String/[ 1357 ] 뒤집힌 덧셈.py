import sys

input = sys.stdin.readline

def rev(x):
    convert = ''
    while x > 0:
        convert += str(x % 10)
        x //= 10

    return int(convert)

X, Y = map(int, input().rstrip().split())
answer = rev(rev(X) + rev(Y))
print(answer)

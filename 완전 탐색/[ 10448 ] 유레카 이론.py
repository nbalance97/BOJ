import sys

start = 1
add = 2
Triangle = []
while True:
    Triangle.append(start)
    start += add
    add += 1
    if start >= 1000:
        break

def check(a, Triangle):
    for i in Triangle:
        if i >= a: continue
        for j in Triangle:
            if j >= a: continue
            for k in Triangle:
                if k >= a: continue
                if i + j + k == a:
                    return True

    return False


count = int(sys.stdin.readline().rstrip())
for i in range(count):
    n = int(sys.stdin.readline().rstrip())
    if check(n, Triangle):
        print(1)
    else:
        print(0)

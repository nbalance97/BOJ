import sys

input = lambda: sys.stdin.readline().rstrip()
N, L = map(int, input().split())

water = list(map(lambda x:int(x)*10, input().split()))
water.sort()
tape = set()
tape_count = 0
for pos in water:
    start = 0
    for i in range(-5, 6):
        if pos+i not in tape:
            start = pos+i
            break
    else:
        continue

    for p in range(start, start+(10*L)+1):
        tape.add(p)
    tape_count += 1

print(tape_count)

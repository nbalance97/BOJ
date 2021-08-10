import sys

K = int(sys.stdin.readline().rstrip())
nodes = list(map(int, sys.stdin.readline().rstrip().split()))

levels = [[] for _ in range(K)]

def visit(level, left, right):
    if left == right:
        levels[level].append(nodes[left])
        return

    mid = (left + right) // 2
    visit(level+1, left, mid-1)
    visit(level+1, mid+1, right)
    levels[level].append(nodes[mid])

visit(0, 0, len(nodes)-1)

for level in levels:
    print(*level)


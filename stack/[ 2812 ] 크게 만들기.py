import sys

input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
number = list(map(int, list(input())))
stack = []
delete_count = 0

for n in number:
    while stack and n > stack[-1] and delete_count < K:
        stack.pop()
        delete_count += 1
    stack.append(n)

if delete_count < K:
    for _ in range(K-delete_count):
        stack.pop()

if len(stack) == 0:
    print(0)
else:
    print("".join(map(str, stack)))

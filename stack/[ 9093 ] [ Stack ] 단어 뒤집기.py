import sys

input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    sentence = input().split()
    stack = []
    for word in sentence:
        convert = ''
        for ch in word:
            stack.append(ch)
        while stack:
            print(stack.pop(), end="")
        print(" ", end="")
    print()
        

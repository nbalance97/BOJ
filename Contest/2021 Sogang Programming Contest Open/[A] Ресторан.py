import sys

input = lambda: sys.stdin.readline().rstrip()

swap = {'B': 'v', 'E': 'ye', 'H': 'n',
        'P': 'r', 'C': 's', 'Y': 'u',
        'X': 'h', 'T': 't', 'A': 'a',
        'K': 'k', 'M': 'm', 'O': 'o'}

answer = "".join([swap[s] for s in input()])
print(answer)

import sys

N = list(map(int, sys.stdin.readline().rstrip().split()))

for _ in range(len(N)):
    swap = False
    for i in range(len(N)-1):
        if N[i] > N[i+1]:
            N[i], N[i+1] = N[i+1], N[i]
            print(*N)

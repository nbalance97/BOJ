import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))

sequence.sort()
answer = []

def recursion(seq, idx):
    global N, M
    if len(seq) == M:
        if seq not in answer:
            print(" ".join(list(map(str, seq))))
            answer.append(seq)
        return
    
    if idx == N:
        return
    
    recursion(seq + [sequence[idx]], idx+1)
    recursion(seq, idx+1)


recursion([], 0)

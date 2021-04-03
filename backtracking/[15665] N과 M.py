import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))

sequence.sort()
answer = set()

def recursion(seq, idx):
    global N, M
    if len(seq) == M:
        answer.add(tuple(seq))
        return
    
    if idx == N:
        return

    recursion(seq + [sequence[idx]], 0) 
    recursion(seq, idx+1) # 안고름


recursion([], 0)

p = list(answer)
p.sort()

# Tuple 앞에 * 붙이면 값만 나옴
for q in p:
    print(*q)

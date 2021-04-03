import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
sequence = list(map(int, sys.stdin.readline().rstrip().split()))

sequence.sort()
answer = set()

def recursion(seq, idx):
    global N, M
    # 중복 제거 할때 가장 좋은 방법은..
    # set에 그냥 넣으면 알아서 중복된거 제거됨. 중복 체크 따로 X
    # list 형식은 set에 못넣으므로 tuple로 변환하여 넣어 줌.
    if len(seq) == M:
        answer.add(tuple(seq))
        return
    
    if idx == N:
        return

    recursion(seq + [sequence[idx]], idx) 
    recursion(seq, idx+1) # 안고름


recursion([], 0)

p = list(answer)
p.sort()

# Tuple 앞에 * 붙이면 값만 나옴
for q in p:
    print(*q)

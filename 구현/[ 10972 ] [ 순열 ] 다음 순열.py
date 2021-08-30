import sys

n = int(sys.stdin.readline().rstrip())

sequence = list(map(int, sys.stdin.readline().rstrip().split()))

def next_permutation(sequence):
    i = len(sequence) - 1
    # sequence[i-1] < sequence[i]인 경우, sequence[i-1]이 바꾸게 될 타겟
    while i > 0 and sequence[i-1] > sequence[i]:
        i = i - 1

    if i == 0:
        return None
    
    swap_pos = i-1
    # 바꾸게 될 타겟보다 큰 값의 위치를 찾음
    j = len(sequence) - 1
    while j > 0 and sequence[swap_pos] >= sequence[j]:
        j = j - 1

    # 두 값을 서로 바꾸어 줌
    sequence[swap_pos], sequence[j] = sequence[j], sequence[swap_pos]
    
    k = len(sequence) - 1
    sequence = sequence[:i] + (sequence[i:])[::-1]        
    return sequence


p = next_permutation(sequence)
if p == None:
    print(-1)
else:
    print(*p)

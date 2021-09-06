import sys
 
n = int(sys.stdin.readline().rstrip())
 
sequence = list(map(int, sys.stdin.readline().rstrip().split()))
 
def prev_permutation(sequence):
    i = len(sequence) - 1

    # sequence[i-1] > sequence[i]인 부분을 찾음 => i-1이 바꿔지게 될 위치임.
    while i > 0 and sequence[i-1] < sequence[i]:
        i = i - 1
 
    if i == 0:
        return None

    swap_pos = i-1
    j = len(sequence) - 1
    # 오른쪽에서 시작했을 때, 바꿔지게 될 요소보다 작은 수들중 처음 나오는 요소가
    # 바뀌어지게 된다.
    while j > 0 and sequence[swap_pos] <= sequence[j]:
        j = j - 1
     
    sequence[swap_pos], sequence[j] = sequence[j], sequence[swap_pos]

    # 바뀌는 점 이후는 내림차순이 되어야 함
    # 위 while문을 보면 알겠지만.. 바뀌는 위치 기준으로 오른쪽은 오름차순이 되어 있음.
    # 따라서, 그냥 뒤집어주면 된다.
    sequence = sequence[:i] + sequence[i:][::-1] 
    return sequence
 
 
p = prev_permutation(sequence)
if p == None:
    print(-1)
else:
    print(*p)

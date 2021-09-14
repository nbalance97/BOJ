
import sys
 
input = lambda :sys.stdin.readline().rstrip()
 
N, K = map(int, input().split())
dolls = list(map(int, input().split()))
answer = int(10e9)
 
lion_pos = []
for i in range(len(dolls)):
    if dolls[i] == 1:
        lion_pos.append(i)
 
left = 0
right = K-1
 
if len(lion_pos) < K:
    print(-1)
else:
    while right < len(lion_pos):
        answer = min(answer, lion_pos[right] - lion_pos[left] + 1)
        left, right = left+1, right+1
    print(answer)

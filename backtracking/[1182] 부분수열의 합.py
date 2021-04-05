import sys

input = sys.stdin.readline
N, S = map(int, input().rstrip().split())
seq = list(map(int, input().rstrip().split()))
seq.sort()

answer = set()

def getCount(idx, s, ans):
    global N, S
    
    if s == S: # 합계가 목표 수치라면 정답에 추가. 단 중복은 제거(set)
        answer.add(tuple(ans))        
        
    # 마지막 요소를 넘게 되면 그냥 return
    if idx == N:
        return

    getCount(idx+1, s+seq[idx], ans+[idx]) # 현재 요소 선택
    getCount(idx+1, s, ans) # 그냥 넘어감

getCount(0, 0, [])

ans = 0
for a in answer:
    if len(a) != 0:
        ans += 1

print(ans)

import sys

input = sys.stdin.readline

n = int(input().rstrip())

is_zero = False
plus = []
minus = []

for _ in range(n):
    t = int(input().rstrip())
    if t > 0:
        plus.append(t)
    elif t < 0:
        minus.append(t)
    else:
        is_zero = True # 0이 있는지 없는지

plus.sort()
plus = plus[::-1]

minus.sort()

answer = 0
q = len(plus)
r = len(minus)

if q % 2 == 1: # 요소가 홀수개면 마지막 요소 미리 더해줌
    answer += plus[-1]
    q = q - 1
    
if r % 2 == 1: 
    if not is_zero: # 0이 있다면 minus에는 0을 곱해서 없애줌.
        answer += minus[-1]
    r = r - 1
    
for i in range(0, q, 2):
    if plus[i+1] == 1: # 곱해지는 수가 1이라면 차라리 더하는게 큼
        answer += (plus[i] + plus[i+1])
    else:
        answer += (plus[i] * plus[i+1])
        
for i in range(0, r, 2):
    answer += (minus[i] * minus[i+1])

print(answer)


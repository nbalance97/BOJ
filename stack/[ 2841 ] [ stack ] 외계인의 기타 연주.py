import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, P = map(int, input().split())
guitar = [deque() for _ in range(7)]

movement = 0

for i in range(N):
    line, pret = map(int, input().split())

    # 스택의 맨 위 요소가 현재 pret보다 작거나 같아질때까지 다 빼줌
    while guitar[line] and guitar[line][-1] > pret:
        guitar[line].pop()
        movement += 1

    # 스택의 맨 위 요소가 현재 pret과 같다면 이미 누른것이므로 생략
    # 아니라면 새로 눌러줘야 함.
    if guitar[line] and guitar[line][-1] == pret:
        continue
    else:
        movement += 1
        guitar[line].append(pret)

print(movement)

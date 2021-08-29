import sys

input = sys.stdin.readline
n = int(input().rstrip())

for _ in range(n):
    S = input().rstrip()

    alpha = set()
    for c in S:
        alpha.add(c)

    answer = 0
    for i in range(ord('A'), ord('Z')+1):
        if chr(i) not in alpha:
            answer += i

    print(answer)
    

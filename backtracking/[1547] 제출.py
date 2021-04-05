import sys

input = sys.stdin.readline

seq = [0, 1, 0, 0]

cnt = int(input().rstrip())
# ㅡㅡ 공이 컵에 붙어 있네
for _ in range(cnt):
    x, y = map(int, input().rstrip().split())
    seq[x], seq[y] = seq[y], seq[x]

for i in range(len(seq)):
    if seq[i] == 1:
        print(i)
        break


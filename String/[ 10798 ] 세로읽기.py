import sys

input = sys.stdin.readline

strlist = [input().rstrip() for _ in range(5)]
max_length = 0
for s in strlist:
    max_length = max(max_length, len(s))

answer = ''
for j in range(max_length):
    for i in range(5):
        if len(strlist[i]) <= j:
            continue
        answer += strlist[i][j]
            
print(answer)

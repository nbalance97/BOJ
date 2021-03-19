import sys

input = sys.stdin.readline
temp = []
for _ in range(9):
    temp.append(int(input().rstrip()))
temp.sort()

answer = []

def dfs(current, sumation, tmp):
    global answer

    if sumation == 100:
        if len(tmp) == 7:
            answer = tmp
            return

    if current == 9 or sumation > 100:
        return
    
    dfs(current+1, sumation, tmp)
    dfs(current+1, sumation+temp[current], tmp + [temp[current]])

    
dfs(0, 0, [])

for a in answer:
    print(a)
    
    

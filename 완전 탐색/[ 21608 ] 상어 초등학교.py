import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
matrix = [[0] * (N+1) for _ in range(N+1)]
students = [list(map(int, input().split())) for _ in range(N**2)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
ht = dict()

for snum, l1, l2, l3, l4 in students:
    c = 0
    l = []
    ht[snum] = [l1, l2, l3, l4]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if matrix[i][j] != 0:
                continue
            lc = 0
            ec = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if nx > 0 and ny > 0 and nx <= N and ny <= N:
                    if matrix[nx][ny] in ht[snum]:
                        lc += 1
                    if matrix[nx][ny] == 0:
                        ec += 1
            if lc == c:
                l.append([i, j, ec])
            elif lc > c:
                c = lc
                l = [[i, j, ec]]
    
    if len(l) == 1:
        matrix[l[0][0]][l[0][1]] = snum
    else:
        me = max(map(lambda x:x[2], l))
        for x, y, ec in l:
            if ec == me:
                matrix[x][y] = snum
                break

answer = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        score = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 1 or ny < 1 or nx > N or ny > N:
                continue
            if matrix[nx][ny] in ht[matrix[i][j]]:
                score += 1
        if score != 0:
            answer += 10 ** (score-1)

print(answer)
    
                

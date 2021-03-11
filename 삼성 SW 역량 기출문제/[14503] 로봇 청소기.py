import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
r, c, d = map(int, input().rstrip().split())

# 0 북 1 동 2 남 3 서

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().rstrip().split())))


rotate = 0
count = 0

while True:
    # 청소 -> 2로 표시, 벽 -> 1
    if matrix[r][c] == 0:
        count += 1
    matrix[r][c] = 2
    # 4방향 조사
    for i in range(4):
        nr = r + dx[(d-i) % 4]
        nc = c + dy[(d-i) % 4]

        # 움직일수 있는 경우 다음 좌표 지정 / 방향 지정
        if matrix[nr][nc] == 0: 
            r = nr
            c = nc
            d = (d - i - 1) % 4
            break
    else:
        # 뒷쪽 방향 조사
        p = (d - 1) % 4
        nr = r + dx[p] 
        nc = c + dy[p]
        if matrix[nr][nc] == 1: # 벽인 경우는 break
            break
        else:
            r = nr
            c = nc
        
            
    

print(count)

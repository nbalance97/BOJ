import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())

matrix = [list(input()) for _ in range(N)]

b_pos = [0, 0]
r_pos = [0, 0]
for i in range(N):
    for j in range(M):
        if matrix[i][j] == 'B':
            b_pos[0], b_pos[1] = i, j
            matrix[i][j] = '.'
        if matrix[i][j] == 'R':
            r_pos[0], r_pos[1] = i, j
            matrix[i][j] = '.'

def bfs(matrix, bpos, rpos):
    queue = deque([[bpos[0], bpos[1], rpos[0], rpos[1], 1]])
    N, M = len(matrix), len(matrix[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = set([(bpos[0], bpos[1], rpos[0], rpos[1])])
    while queue:
        b_x, b_y, r_x, r_y, cost = queue.popleft()
        b_pos,r_pos = [b_x, b_y], [r_x, r_y]
        if cost == 11:
            break
        for i in range(4):
            bx, by = b_pos
            rx, ry = r_pos
            b_finish, r_finish = False, False
            b_end, r_end = False, False
            while True:
                # 벽을 만날때까지 파란 공 이동
                if matrix[bx + dx[i]][by + dy[i]] != '#':
                    bx, by = bx + dx[i], by + dy[i]
                else:
                    b_end = True

                # 벽을 만나거나 구멍을 만날때까지 빨간 공 이동
                if matrix[rx + dx[i]][ry + dy[i]] != '#' and not r_finish:
                    rx, ry = rx + dx[i], ry + dy[i]
                else:
                    r_end = True

                # 빨간공과 파란공이 만났을 때
                if rx == bx and ry == by:
                    if r_finish: # 빨간색이 구멍에 들어간 경우 파란공도 들어가는 것
                        b_finish = True
                    # 이미 빨간공이 멈춰선 경우 파란공 위치 조정
                    if r_end:
                        bx, by = bx - dx[i], by - dy[i]
                    # 이미 파란공이 멈춰선 경우 빨간공 위치 조정
                    elif b_end:
                        rx, ry = rx - dx[i], ry - dy[i]
                    break

                # 파란공이 구멍에 들어간 경우 finish 처리
                if matrix[bx][by] == 'O':
                    b_finish = True
                    break
                
                # 빨간공이 구멍에 들어간 경우 finish 처리
                if matrix[rx][ry] == 'O':
                    r_finish = True

                # 둘다 벽을 만난 경우 종료
                if b_end and r_end:
                    break
                
            # 빨간공은 들어가고 파란공은 들어가지 않은 경우 거리 리턴
            if r_finish and not b_finish:
                return cost

            # set에 방문기록 저장 (재방문하지 않도록)
            if (bx, by, rx, ry) not in visited and not b_finish:
                visited.add((bx, by, rx, ry))
                queue.append([bx, by, rx, ry, cost+1])

    return -1

print(bfs(matrix, b_pos, r_pos))

                

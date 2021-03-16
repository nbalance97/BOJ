import sys
import copy

input = sys.stdin.readline
R, C, T = map(int, input().rstrip().split())

matrix = []
for _ in range(R):
    matrix.append(list(map(int, input().rstrip().split())))

def spread():
    global R, C
    copy_matrix = copy.deepcopy(matrix)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(R):
        for j in range(C):
            if copy_matrix[i][j] != 0 and copy_matrix[i][j] != -1:
                p = copy_matrix[i][j] // 5
                count = 0
                for k in range(4):
                    t1 = i + dx[k]
                    t2 = j + dy[k]
                    if t1 >= 0 and t1 <= R-1 and t2 >= 0 and t2 <= C-1:
                        if copy_matrix[t1][t2] != -1:
                            matrix[t1][t2] += p
                            count += 1

                matrix[i][j] -= copy_matrix[i][j] # 원값 빼줌
                matrix[i][j] += (copy_matrix[i][j] - p * count) # 빠진값 더해줌
    

def roll(x, topdown):
    # y는 항상 0임. 문제에 있음.
    global R, C
    flg = False
    xC, yC = 0, 0
    cX, cY = x, 0
    if topdown: # True -> Top
        xC = -1
        yC = 1 # 변화상수
    else:
        xC = 1
        yC = 1
        
    # y축 종료 시 종료된 값 이어서 x축에서도 써야 하므로
    # temp 변수 따로 둠
    temp = 0
    while True:
        while True:
            cY = cY + yC
            if cY >= 0 and cY <= C-1:        
                tmp = matrix[cX][cY]
                matrix[cX][cY] = temp
                temp = tmp
            else:
                if cY == C:
                    cY -= 1
                else:
                    cY += 1
                break
        
        yC = -yC # 부호 전환

        while True:
            cX = cX + xC
            if cX >= 0 and cX <= R-1:
                if matrix[cX][cY] == -1:
                    flg = True
                    break
                tmp = matrix[cX][cY]
                matrix[cX][cY] = temp
                temp = tmp
            else:
                if cX == R:
                    cX -= 1
                else:
                    cX += 1
                break
                    
        if flg: break
        xC = -xC # 부호 전환

def sumation():
    global R, C
    t = 0
    for i in range(R):
        for j in range(C):
            if matrix[i][j] != -1:
                t += matrix[i][j]
                
    return t

top = 0
down = 0
for i in range(R): # 공기청정기의 top, down 구함
    if matrix[i][0] == -1:
        top = i
        down = i +1
        break

for i in range(T):
    spread()
    roll(top, True)
    roll(down, False)

print(sumation())



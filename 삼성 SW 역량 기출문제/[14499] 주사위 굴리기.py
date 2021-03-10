import sys

input = sys.stdin.readline

Map = []
N, M, x, y, K = map(int, input().rstrip().split())
for _ in range(N):
    Map.append(list(map(int, input().rstrip().split())))
    
command = list(map(int, input().rstrip().split()))

up, down, east, west, front, back = 0, 0, 0, 0, 0, 0
for com in command:
    check = False
    if com == 4 and x < N-1: # 남쪽
        x = x + 1
        front, down, back, up = up, front, down, back
        check = True
        
    if com == 3 and x > 0: # 북쪽
        x = x - 1
        front, down, back, up = down, back, up, front
        check = True
        
    if com == 2 and y > 0: # 서쪽
        y = y - 1
        west, down, east, up = up, west, down, east
        check = True
        
    if com == 1 and y < M-1: # 동쪽
        y = y + 1
        west, down, east, up = down, east, up, west
        check = True

    if check:
        temp = Map[x][y]
        if Map[x][y] == 0:
            # 해당 칸의 값이 0이면 
            Map[x][y] = down
        else:
            down = Map[x][y]
            Map[x][y] = 0
        print(up)

            

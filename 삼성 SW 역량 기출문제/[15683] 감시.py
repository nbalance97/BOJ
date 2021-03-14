import sys

input = sys.stdin.readline
N, M = map(int, input().rstrip().split())

office = []

for _ in range(N):
    office.append(list(map(int, input().rstrip().split())))

cctv = [] # 1번~5번 cctv

for i in range(N):
    for j in range(M):
        if office[i][j] != 0 and office[i][j] != 6:
            cctv.append([i, j, office[i][j]]) # 인덱스와 cctv 번호 저장

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# cctv 설치 시 감지 가능한 공간은 훑고 지나갈때마다 -1 해주는 방식으로.

answer = sys.maxsize

def dfs(idx):
    global answer
    
    if idx == len(cctv):
        answer = min(answer, check())
        return



    x, y, cctv_idx = cctv[idx]
    if cctv_idx == 1: # 한방향 검색
        left(x, y, False)
        dfs(idx + 1)
        left(x, y, True)
        
        right(x, y, False)
        dfs(idx + 1)
        right(x, y, True)

        top(x, y, False)
        dfs(idx + 1)
        top(x, y, True)

        down(x, y, False)
        dfs(idx + 1)
        down(x, y, True)
    elif cctv_idx == 2: # 양방향 검색
        left(x, y, False)
        right(x, y, False)
        dfs(idx + 1)
        left(x, y, True)
        right(x, y, True)

        top(x, y, False)
        down(x, y, False)
        dfs(idx + 1)
        top(x, y, True)
        down(x, y, True)
    elif cctv_idx == 3: # 두방향(직각)
        left(x, y, False)
        top(x, y, False)
        dfs(idx + 1)
        
        left(x, y, True)
        right(x, y, False)
        dfs(idx + 1)

        top(x, y, True)
        down(x, y, False)
        dfs(idx + 1)

        right(x, y, True)
        left(x, y, False)
        dfs(idx + 1)


        left(x, y, True)
        down(x, y, True) 
    elif cctv_idx == 4: # 세방향
        # ^
        left(x, y, False)
        top(x, y, False)
        right(x, y, False)
        dfs(idx + 1)

        # >
        left(x, y, True)
        down(x, y, False)
        dfs(idx + 1)

        # v
        top(x, y, True)
        left(x, y, False)
        dfs(idx + 1)

        # <
        right(x, y, True)
        top(x, y, False)
        dfs(idx + 1)

        top(x, y, True)
        left(x, y, True)
        down(x, y, True)
    elif cctv_idx == 5:
        top(x, y, False)
        down(x, y, False)
        left(x, y, False)
        right(x, y, False)
        dfs(idx + 1)
        top(x, y, True)
        down(x, y, True)
        left(x, y, True)
        right(x, y, True)

def check():
    global N, M
    count = 0
    for i in range(N):
        for j in range(M):
            if office[i][j] == 0:
                count += 1
                
    return count

def left(x, y, isRollback):
    # isRollback이 True이면 다시 원래값으로 복구
    # True가 아니라면 cctv 설치했을때 경우
    
    for i in range(y-1, -1, -1):
        if office[x][i] == 6:
            break
        else:
            if 1 <= office[x][i] and office[x][i] <= 5:
                continue
            if not isRollback:
                office[x][i] -= 1
            else:
                office[x][i] += 1

def right(x, y, isRollback):
    global N, M
    for i in range(y+1, M):
        if office[x][i] == 6:
            break
        if 1 <= office[x][i] and office[x][i] <= 5:
            continue
        if not isRollback:
            office[x][i] -= 1
        else:
            office[x][i] += 1

def top(x, y, isRollback):
    global N,M
    for i in range(x-1, -1, -1):
        if office[i][y] == 6:
            break
        if 1 <= office[i][y] and office[i][y] <= 5:
            continue
        if not isRollback:
            office[i][y] -= 1
        else:
            office[i][y] += 1

def down(x, y, isRollback):
    global N, M
    for i in range(x+1, N):
        if office[i][y] == 6:
            break
        if 1 <= office[i][y] and office[i][y] <= 5:
            continue
        if not isRollback:
            office[i][y] -= 1
        else:
            office[i][y] += 1

dfs(0)
print(answer)        


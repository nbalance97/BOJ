import sys
from collections import deque

# 1. deque 내용 옮길때 주의해서 옮기기 ..
# 2. 오리가 있는 위치도 호수로 생각하고 풀어야 함.
# 3. 시간 초과가 나므로 효율적으로 풀이해야 함 -> 매번 bfs하는것이 아니라 매 타임이 끝날 때 다음에 방문해야 하는
#    지점들을 따로 저장한 다음, 다음 타임때 저장한 부분만 불러와서 처리


R, C = map(int, sys.stdin.readline().rstrip().split())
lake = [["."] * (C+1)]
for _ in range(R):
    lake.append(["."] + list(map(str, " ".join(sys.stdin.readline().rstrip()).split())))

duckqueue = deque()
duckvisited = [[False] * (C+1) for _ in range(R+1)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 처음 오리가 갈수있는 경로들 다 가보고 다음에 갈수 있는 경로들 저장
def init(L1, L2):
    global R, C
    x1, y1 = L1
    x2, y2 = L2
    
    queue = deque()
    queue.append([x1, y1])
    duckvisited[x1][y1] = True
    
    while queue:
        cX, cY = queue.popleft()
        if cX == x2 and cY == y2:
            return True
        for i in range(4):
            nX = cX + dx[i]
            nY = cY + dy[i]
            if 1 <= nX <= R and 1 <= nY <= C:
                if not duckvisited[nX][nY] and lake[nX][nY] != 'X':
                    queue.append([nX, nY])
                    duckvisited[nX][nY] = True
                elif not duckvisited[nX][nY] and lake[nX][nY] == 'X':
                    duckqueue.append([nX, nY])
                    duckvisited[nX][nY] = True
    return False


# 두개의 오리가 서로 접근 가능한지 확인 / 다음 번에 오리가 갈 경로 저장
def check(L2):
    newQueue = deque() # 다음에 방문할 queue
    x2, y2 = L2
    while duckqueue:
        cX, cY = duckqueue.popleft()
        if cX == x2 and cY == y2:
            return True

        if lake[cX][cY] != "X":
            for i in range(4):
                nX = cX + dx[i]
                nY = cY + dy[i]
                if 1 <= nX <= R and 1 <= nY <= C:
                    if not duckvisited[nX][nY] and lake[nX][nY] != "X":
                        duckqueue.append([nX, nY]) # 열려있는 경로들은 모두 탐색
                        duckvisited[nX][nY] = True
                    elif not duckvisited[nX][nY] and lake[nX][nY] == "X": # 닫혀있으면 다음 후보에
                        newQueue.append([nX, nY])
                        duckvisited[nX][nY] = True
        else:
            newQueue.append([cX, cY])
            
    while newQueue: # deque 옮길떄 이렇게 옮겨야 ..
        duckqueue.append(newQueue.popleft()) # 방문 큐 갱신
        
    return False
            
            

def bfs():
    global R, C
    queue = deque()
    L1 = None
    L2 = None

    # 초기 
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if lake[i][j] == '.' or lake[i][j] == "L":
                queue.append([i, j])

            if lake[i][j] == "L" and L1 is None:
                L1 = [i, j]
            elif lake[i][j] == "L" and L1 is not None:
                L2 = [i, j]

    time = -1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[False] * (C + 1) for _ in range(R + 1)]

    if init(L1, L2): # 바로 만난다면 0 리턴
        return 0

    t = 0
    while True:
        t = t + 1
        for i in range(len(queue)):
            cx, cy = queue.popleft()
	    
	    # 인접 빙판 녹게 하기
            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]
                if 1 <= nx <= R and 1 <= ny <= C and lake[nx][ny] == 'X' and not visited[nx][ny]:
                    lake[nx][ny] = '.'
                    visited[nx][ny] = True # 녹인 경우 방문하지 않도록
                    queue.append([nx, ny])
                    
        if check(L2):
            return t

print(bfs())

import sys
from collections import deque

input = sys.stdin.readline
matrix = [['.'] * 7]

# list('abc') ==> ['a', 'b', 'c'].. 꿀팁!!
for _ in range(12):
    matrix.append(['.'] + list(input().rstrip()))

visited = [[False] * 7 for _ in range(13)]

def bfs(cx, cy):
    same = []
    color = matrix[cx][cy]
    queue = deque()
    queue.append([cx, cy])
    visited[cx][cy] = True
    same.append([cx, cy])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 1 and nx <= 12 and ny >= 1 and ny <= 6:
                if matrix[nx][ny] == color and not visited[nx][ny]:
                    queue.append([nx, ny])
                    same.append([nx, ny])
                    visited[nx][ny] = True

    if len(same) >= 4:
        for x, y in same:
            matrix[x][y] = '.'
        return True
    else:
        return False

def boom():
    is_flag = False
    for i in range(1, 13):
        for j in range(1, 7):
            if matrix[i][j] != '.' and not visited[i][j]:
                is_flag = (bfs(i,j) or is_flag)
                # or연산자의 경우 앞에것이 true면 뒤에걸 안봐요..

    return is_flag

# 여기까지 구현하고 느낀게.. 행이랑 열 바꿨으면 훨 쉬웟겟다 ㅡㅡ
def todown():
    for j in range(1, 7):
        p = [s[j] for s in matrix] # 열별로 값 가져
        p = list(filter(lambda x:x != '.', p))
        p = ['.'] * (13-len(p)) + p
        for i in range(1, 13):
            visited[i][j] = False
            matrix[i][j] = p[i]
            
boom_count = 0
while True:
    t = boom()
    if t == False:
        break
    boom_count += 1
    todown()

print(boom_count)


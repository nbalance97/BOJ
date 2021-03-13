import sys


N, M = map(int, sys.stdin.readline().rstrip().split())

paper = []

for _ in range(N):
    paper.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * M for _ in range(N)]

max_sum = 0

def dfs(i, j, step):    
    N = len(paper)
    M = len(paper[0])

    max_value = 0
    
    if step == 4:
        return paper[i][j]
    
    for n in range(4):
        nx = i + dx[n]
        ny = j + dy[n]
        if 0 <= nx and nx < N and 0 <= ny and ny < M:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                max_value = max(max_value, paper[i][j] + dfs(nx, ny, step+1))
                visited[nx][ny] = False
                
    return max_value

# dfs로는 ㅗ모양 확인이 어려움 ..
def check(i, j): # ㅗ모양 체크 함수
    global N, M
    
    # 가운데 i,j를 포함한 경우
    chkarr = [[[i, j], [i-1, j], [i+1, j], [i, j+1]], # ㅏ
              [[i, j], [i, j-1], [i, j+1], [i+1, j]], # ㅜ
              [[i, j], [i-1, j], [i+1, j], [i, j-1]], # ㅓ
              [[i, j], [i, j+1], [i, j-1], [i-1, j]]] # ㅗ

    midsum = 0
    for chk in chkarr:
        temp = 0
        for x, y in chk:
            if x >= 0 and x < N and y >= 0 and y < M:
                temp += paper[x][y]
            else:
                break
        else: # 온전히 반복문이 마쳤다면(4개 모두 조건에 안걸린 경우)
            midsum = max(temp, midsum)

    return midsum # ㅗ모양으로 가능한 최대합 리턴
    
answer = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        answer = max(answer, dfs(i, j, 1)) # 일반적인 모양들 체크
        visited[i][j] = False
        answer = max(answer, check(i, j)) # ㅗ모양 체크
                    
print(answer)
        

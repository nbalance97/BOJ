import sys

input = lambda: sys.stdin.readline().rstrip()

INT_MAX = int(10e9)
n, m = map(int, input().split())

matrix = [[INT_MAX] * (n+1) for _ in range(n+1)]
answer = [[0] * (n+1) for _ in range(n+1)]
for i in range(n+1):
    matrix[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a][b] = min(matrix[a][b], c)
    matrix[b][a] = min(matrix[b][a], c)
    answer[a][b] = b
    answer[b][a] = a


# 최단거리 구하는 파트
# 최단거리 구하면서 거리 갱신 시 어느 노드를 들리는지 정보 저장
for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if matrix[j][k] > matrix[j][i] + matrix[i][k]:
                matrix[j][k] = matrix[j][i] + matrix[i][k]
                answer[j][k] = i

# 다른 노드를 들리게 되는 경우,
# 거슬러 올라가서 가장 먼저 거쳐야 하는 집하장으로 바꾸어 줌
for i in range(1, n+1):
    for j in range(1, n+1):
        if answer[i][j] == 0:
            answer[i][j] = '-'
            continue
        p = answer[i][j]
        while p != answer[i][p]:
            p = answer[i][p]
        answer[i][j] = p

for a in answer[1:]:
    print(*a[1:])

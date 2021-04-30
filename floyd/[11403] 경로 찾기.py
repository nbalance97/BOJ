import sys

input = sys.stdin.readline
matrix = []

n = int(input().rstrip())
for i in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

# floyd Algorithm
# j -> i -> k로 가는게 j -> k보다 빠르다면 갱신하는 방식인데..
# 이번 예제에서는 그냥 단순히 경로 존재 여부이므로 2일 경우 1로 수정하는 방식
for i in range(n):
    for j in range(n):
        for k in range(n):
            if matrix[j][i] + matrix[i][k] == 2:
                matrix[j][k] = 1

for i in range(n):
    print(*matrix[i])

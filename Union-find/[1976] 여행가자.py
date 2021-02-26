import sys

def find(parent, a):
    if parent[a] != a:
        parent[a] = find(parent, parent[a])

    return parent[a]

def union(parent, a, b):
    t1 = find(parent, a)
    t2 = find(parent, b)

    if t1 != t2:
        parent[t1] = parent[t2]

input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
matrix = []
matrix.append([0] * (n+1))
for _ in range(n):
    matrix.append([0] + list(map(int, input().rstrip().split())))

parent = [i for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if matrix[i][j] == 1:
            if find(parent, i) != find(parent, j):
                union(parent, i, j)


question = list(map(int, input().rstrip().split()))

p = find(parent, question[0])

for i in range(1, len(question)):
    if find(parent, question[i]) != p:
        print("NO")
        break
else:
    print("YES")

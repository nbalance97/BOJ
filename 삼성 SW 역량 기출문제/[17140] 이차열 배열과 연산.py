import sys
from collections import Counter

def Rop(matrix):
    p = []
    maxlen = 0
    for mat in matrix:
        temp = []
        q = Counter(mat)
        q = list(filter(lambda x:x[0]!=0, q.items()))
        q = sorted(q, key=lambda x:(x[1], x[0])) # 수의 등장 순서, 수 순 정렬
        for a, b in q:
            temp.append(a)
            temp.append(b)
        if len(temp) > 100:
            temp = temp[:100]
        p.append(temp)
        maxlen = max(maxlen, len(temp))
    return (p, maxlen)

def Rcoordi(matrix, maxlen):
    for i in range(len(matrix)):
        if len(matrix[i]) < maxlen:
            matrix[i] = matrix[i] + ([0] * (maxlen - len(matrix[i])))

def Cop(matrix):
    ans = []
    maxlen = 0
    for y in range(len(matrix[0])):
        temp = []
        for x in range(len(matrix)):
            temp.append(matrix[x][y])
        q = Counter(temp)
        q = list(filter(lambda x:x[0]!=0, q.items()))
        q = sorted(q, key=lambda x:(x[1], x[0])) # 수의 등장 순서, 수 순 정렬
        temp = []
        for a, b in q:
            temp.append(a)
            temp.append(b)
        if len(temp) > 100:
            temp = temp[:100]
        ans.append(temp)
        maxlen = max(maxlen, len(temp))
    return (ans, maxlen)

def Ccoordi(matrix, maxlen):
    Rcoordi(matrix, maxlen)
    temp = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            temp[i][j] = matrix[j][i]
    return temp
            
r, c, k = map(int, sys.stdin.readline().rstrip().split())
matrix = [list(map(int, sys.stdin.readline().rstrip().split())) for i in range(3)]

answer = 0
while True:
    if len(matrix[0]) > c-1 and len(matrix) > r-1 and matrix[r-1][c-1] == k:
        break
    answer = answer + 1
    if answer > 100:
        answer = -1
        break
    
    if len(matrix) >= len(matrix[0]):
        matrix, maxlen = Rop(matrix)
        Rcoordi(matrix, maxlen)
    else:
        matrix, maxlen = Cop(matrix)
        matrix = Ccoordi(matrix, maxlen)
    
    
print(answer)

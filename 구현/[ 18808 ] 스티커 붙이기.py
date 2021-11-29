import sys

n, m, k = map(int, input().split())

matrix = [[0] * m for _ in range(n)]

stickers = []
for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(sticker)

def rotate(sticker):
    new_sticker = [[0] * len(sticker) for _ in range(len(sticker[0]))]
    for i in range(len(new_sticker)):
        for j in range(len(new_sticker[0])):
            new_sticker[i][j] = sticker[len(sticker)-1-j][i]

    return new_sticker

def test(sticker, a, b):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1 and matrix[a+i][b+j] == 1:
                return False
    return True

def set_value(sticker, a, b):
    for i in range(len(sticker)):
        for j in range(len(sticker[0])):
            if sticker[i][j] == 1:
                matrix[a+i][b+j] = 1

for sticker in stickers:
    temp = sticker
    end = False
    for _ in range(4):
        for i in range(n):
            for j in range(m):
                if i + len(temp) > n or j + len(temp[0]) > m:
                    continue
                if test(temp, i, j):
                    set_value(temp, i, j)
                    end = True
                    break
            if end:
                break
        if end:
            break

        temp = rotate(temp)

answer = 0
for m in matrix:
    answer += sum(m)

print(answer)

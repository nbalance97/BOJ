import sys

input = lambda : sys.stdin.readline().rstrip()

matrix = [list(map(int, input().split())) for _ in range(10)]

card_count = [0, 5, 5, 5, 5, 5] # 각 색종이 개수

min_card_count = int(10e9)

def check_card(x, y, size):
    if x+size > len(matrix) or y+size > len(matrix[0]):
        return False
    
    for i in range(x, x+size):
        for j in range(y, y+size):
            if matrix[i][j] == 0:
                return False
    return True

def set_value_to_matrix(x, y, size, value):
    if x+size > len(matrix) or y+size > len(matrix[0]):
        return
    for i in range(x, x+size):
        for j in range(y, y+size):
            matrix[i][j] = value

def check_finish():
    p = sum([p for m in matrix for p in m if p == 1])
    if p > 0:
        return False
    else:
        return True

def get_card_count():
    total_card_count = 0
    for i in range(1, 6):
        total_card_count += (5 - card_count[i])
    return total_card_count

def dfs(a, b):
    global min_card_count
    for i in range(a, len(matrix)):
        for j in range(b, len(matrix[0])):
            if matrix[i][j] == 1:
                for card in range(1, 6):
                    if not check_card(i, j, card):
                        return   
                    if card_count[card] > 0:
                        card_count[card] -= 1
                        set_value_to_matrix(i, j, card, 0)
                        dfs(i, 0)
                        set_value_to_matrix(i, j, card, 1)
                        card_count[card] += 1

                return
                        
    if check_finish():
        min_card_count = min(min_card_count, get_card_count())

dfs(0, 0)
if min_card_count == int(10e9):
    print(-1)
else:
    print(min_card_count)

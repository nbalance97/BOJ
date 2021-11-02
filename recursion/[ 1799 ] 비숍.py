import sys

input = lambda : sys.stdin.readline()

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

bishop = set()
white_bishop_list = [(x, y) for x in range(n) for y in range(n) if matrix[x][y] == 1 and (x+y)%2 == 0]
black_bishop_list = [(x, y) for x in range(n) for y in range(n) if matrix[x][y] == 1 and (x+y)%2 == 1]

save = [0]

def solve(bishoppos, color):
    can_bishop_list = []
    if color == 0:
        can_bishop_list = white_bishop_list
    else:
        can_bishop_list = black_bishop_list
    
    if bishoppos == len(can_bishop_list):
        save[0] = max(save[0], len(bishop))
        return

    current = can_bishop_list[bishoppos]
    can = True
    for x, y in bishop:
        if abs(x-current[0]) == abs(y-current[1]):
            can = False
            break

    if can:
        bishop.add((current[0], current[1]))
        solve(bishoppos+1, color)
        bishop.remove((current[0], current[1]))
    solve(bishoppos+1, color)

answer = 0
# white
solve(0, 0)
answer += save[0]

# black
save[0] = 0
bishop = set()
solve(0, 1)
answer += save[0]

print(answer)

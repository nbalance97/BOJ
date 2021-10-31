import sys

input = lambda: sys.stdin.readline().rstrip()

def convert(way):
    return (way + 1) % 4

def get_movement(d, g):
    mv = [d]
    for _ in range(g):
        new_mv = []
        for i in range(len(mv)-1, -1, -1):
            new_mv.append(convert(mv[i]))
        mv += new_mv
        
    return mv

line_information = set()

N = int(input())

for _ in range(N):
    x, y, d, g = map(int, input().split())
    movement = get_movement(d, g)

    for move in movement:
        nx, ny = x, y
        if move == 0:
            nx = x + 1
        elif move == 1:
            ny = y - 1
        elif move == 2:
            nx = x - 1
        elif move == 3:
            ny = y + 1
            
        line_information.add((x, y))
        line_information.add((nx, ny))
        x, y = nx, ny
        
answer = 0
for i in range(101):
    for j in range(101):
        if (i, j) in line_information and \
           (i+1, j) in line_information and \
           (i+1, j+1) in line_information and \
           (i, j+1) in line_information:
            answer += 1

print(answer)

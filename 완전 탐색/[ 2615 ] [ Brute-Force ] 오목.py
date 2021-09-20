import sys

input = lambda :sys.stdin.readline().rstrip()

matrix = [list(map(int, input().split())) for _ in range(19)]
visited = [[[False] * 4 for _ in range(19)] for _ in range(19)]

def check(matrix, visited, x, y):
    direction = [[1, -1], [1, 0], [0, 1], [1, 1]]
    p = matrix[x][y]

    for idx, d in enumerate(direction):
        temp_x, temp_y = x, y
        if visited[temp_x][temp_y][idx]:
            continue
        visited[temp_x][temp_y][idx] = True
        count = 1
        while True:
            temp_x, temp_y = temp_x + d[0], temp_y + d[1]
            if 0 <= temp_x and temp_x < 19 and 0 <= temp_y and temp_y < 19:
                if matrix[temp_x][temp_y] == p:
                    visited[temp_x][temp_y][idx] = True
                    count += 1
                else:
                    break
            else:
                break
            if count >= 6:
                break

        if count == 5:
            if d[0] == 1 and d[1] == -1:
                return [x+4, y-4]
            return [x, y]
        
    return None

end = False
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] != 0:
            result = check(matrix, visited, i, j)
            if result is not None:
                i, j = result
                print(matrix[i][j])
                print(i+1, j+1)
                end = True
        if end:
            break
    if end:
        break

if not end:
    print(0)
            

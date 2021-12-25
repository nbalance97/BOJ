import sys

input = lambda: sys.stdin.readline().rstrip()
W, H, X, Y, P = map(int, input().split())

def compare_square(point, x, y, w, h):
    return x <= point[0] and point[0] <= x+w \
           and y <= point[1] and point[1] <= y+h

radius = H // 2
dist = radius ** 2

def compare_circle(point):
    circle_point1 = [X, Y+radius]
    circle_point2 = [X+W, Y+radius]

    dist1 = (circle_point1[0] - point[0]) ** 2 + \
            (circle_point1[1] - point[1]) ** 2
    dist2 = (circle_point2[0] - point[0]) ** 2 + \
            (circle_point2[1] - point[1]) ** 2

    return dist1 <= dist or dist2 <= dist

answer = 0
for _ in range(P):
    a, b = map(int, input().split())
    if compare_square([a, b], X, Y, W, H) or compare_circle([a, b]):
        answer += 1

print(answer)
        

    

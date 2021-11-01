import sys
import heapq
import math
 
input = lambda : sys.stdin.readline().rstrip()
 
def calculate_distance(src, dest):
    return math.sqrt((src[0]-dest[0]) ** 2 + (src[1]-dest[1]) ** 2)
 
myX, myY = map(float, input().split())
targetX, targetY = map(float, input().split())
N = int(input())
 
points = [list(map(float, input().split())) for _ in range(N)]
points = [[myX, myY]] + points + [[targetX, targetY]]
 
time_matrix = [[0] * (N+2) for _ in range(N+2)]
 
for i in range(len(points)):
    for j in range(i+1, len(points)):
        if i == 0:
            time_matrix[i][j] = calculate_distance(points[i], points[j]) / 5
        else:
            distance = calculate_distance(points[i], points[j])
            time_matrix[i][j] = distance / 5
            if distance > 50.0:
                time_matrix[i][j] = min(time_matrix[i][j],
                                        2 + (distance-50) / 5)
            elif distance == 50.0:
                time_matrix[i][j] = 2.0
            else:
                time_matrix[i][j] = min(time_matrix[i][j],
                                        2 + (50-distance) / 5)
        time_matrix[j][i] = time_matrix[i][j]
        
INT_MAX = int(10e9)
distance = [INT_MAX] * (N+2)
distance[0] = 0
heap = [[0, 0]]
 
while heap:
    time, next_node = heapq.heappop(heap)
    if distance[next_node] != time:
        continue
 
    for i in range(len(points)):
        if next_node == i:
            continue
        if distance[i] > time + time_matrix[i][next_node]:
            distance[i] = time + time_matrix[i][next_node]
            heapq.heappush(heap, [distance[i], i])
 
print("%.6f"%(distance[N+1]))

import sys

input = sys.stdin.readline

t = int(input().rstrip())

succeed = False

def get_manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def dfs(visited, stations, current, festival):
    global succeed

    if get_manhattan_distance(current, festival) <= 1000:
        succeed = True
        return

    for i in range(len(stations)):
        if tuple(stations[i]) not in visited and (
            get_manhattan_distance(current, stations[i]) <= 1000
        ):
            visited.add(tuple(stations[i]))
            dfs(visited, stations, stations[i], festival)
            if succeed:
                return
        
    

for _ in range(t):
    n = int(input().rstrip())
    start = list(map(int, input().rstrip().split()))
    stations = []
    for __ in range(n):
        stations.append(list(map(int, input().rstrip().split())))
    festival = list(map(int, input().rstrip().split()))
    succeed = False
    dfs(set(), stations, start, festival)
    if succeed:
        print('happy')
    else:
        print('sad')

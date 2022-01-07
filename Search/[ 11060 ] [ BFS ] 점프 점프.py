import sys
from collections import deque

def bfs(dist, start, end):
    queue = deque([[start, 0]])
    visited = [False] * (end+1)
    visited[start] = True
    
    while queue:
        pos, movement = queue.popleft()
        if pos == end:
            return movement
        for i in range(1, dist[pos]+1):
            if pos + i <= end:
                if not visited[pos+i]:
                    visited[pos + i] = True
                    queue.append([pos+i, movement+1])
                    
    return -1

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A = list(map(int, input().split()))

print(bfs(A, 0, N-1))

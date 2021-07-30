import sys

input = sys.stdin.readline

T = int(input().rstrip())

def dfs(visited, sequence, start, current):
    if visited[current] == True:
        return False
    visited[current] = True
    if current == start:
        return True
    return dfs(visited, sequence, start, sequence[current])

for _ in range(T):
    N = int(input().rstrip())
    sequence = [0] + list(map(int, input().rstrip().split()))
    visited = [False] * (N+1)
    answer = 0
    for i in range(1, N+1):
        if visited[i] == False:
            answer += 1
            dfs(visited, sequence, i, sequence[i])
    print(answer)

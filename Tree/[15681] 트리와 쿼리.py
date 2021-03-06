import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, R, Q = map(int, input().rstrip().split())
Tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    s, e = map(int, input().rstrip().split())
    # 양방향 트리이므로 양쪽에 넣어줌
    Tree[s].append(e)
    Tree[e].append(s)

INF = sys.maxsize
memoization = [0] * (N+1) # 서브트리의 개수 기록

def dfs(node):
    memoization[node] = 1

    for next_ in Tree[node]:
        if memoization[next_] == 0: # memoization 값이 0이라는 것은 방문하지 않은 노드라는 것이므로 방문
            memoization[node] += dfs(next_) # 자식 노드의 서브 트리 개수 더함

    return memoization[node]

dfs(R)

for _ in range(Q):
    question = int(input().rstrip())
    print(memoization[question])
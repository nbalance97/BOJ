import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
truth = set()
party = []
visited = [False] * (M)
temp = list(map(int, input().split()))
truth |= set(temp[1:])
for _ in range(M):
    party.append(set(list(map(int, input().split()))[1:]))

while True:
    cf = False
    for i in range(len(party)):
        if not visited[i] and len(party[i] & truth) != 0:
            cf = True
            visited[i] = True
            truth |= party[i]
    if not cf:
        break

answer = 0
for i in range(M):
    if not visited[i]:
        answer += 1

print(answer)
            

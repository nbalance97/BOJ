import sys
import heapq

input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
INT_MAX = int(10e9)

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().rstrip().split())
    graph[a].append([b, c])

start, end = map(int, input().rstrip().split())
distance = [INT_MAX] * (n+1)
parent = [i for i in range(n+1)]
distance[start] = 0
candidate = [[0, start]]
while candidate:
    dist, node = heapq.heappop(candidate)
    if dist > distance[node]:
        # 갱신된 경우에는 넘겨줌
        continue
    for next_node, cost in graph[node]:
        if dist + cost < distance[next_node]:
            distance[next_node] = dist + cost
            parent[next_node] = node
            heapq.heappush(candidate, [distance[next_node], next_node])

print(distance[end])
answer = []
temp = end
while parent[temp] != temp:
    answer.append(temp)
    temp = parent[temp]
answer.append(start)
print(len(answer))
answer.reverse()
print(" ".join(list(map(str, answer))))

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
people = set(input().split())
child = {person:[] for person in people}
edge = {person:[] for person in people}
indegree = {person:0 for person in people}
father = []

M = int(input())
for _ in range(M):
    a, b = input().split()
    indegree[a] += 1
    edge[b].append(a)
    
queue = deque()
for person in people:
    if indegree[person] == 0:
        queue.append(person)
        father.append(person)
        
while queue:
    node = queue.popleft()
    for next_node in edge[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)
            child[node].append(next_node)

print(len(father))
print(*sorted(father))
for name in sorted(list(people)):
    print_str = name + " " + str(len(child[name]))
    if len(child[name]) != 0:
        print_str += (" " + " ".join(sorted(child[name])))
    print(print_str)

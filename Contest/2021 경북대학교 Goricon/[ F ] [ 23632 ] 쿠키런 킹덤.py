import sys

input = lambda: sys.stdin.readline().rstrip()
n, m, t = map(int, input().split())
building = list(map(int, input().split()))
have = [[]]
needs = [set() for _ in range(n+1)]
resources = set()
visited = set()

for i in range(n):
    temp = list(map(int, input().split()))[1:]
    have.append(temp)
    
for i in range(n-m):
    temp = list(map(int, input().split()))
    needs[temp[0]] |= set(temp[2:])

for i in building:
    visited.add(i)
    resources |= set(have[i])

time = 0

while True:
    if time == t:
        break
    add_resource = set()
    flag = True
    for i in range(1, n+1):
        if i not in visited and needs[i] & resources == needs[i]:
            flag = False
            visited.add(i)
            add_resource |= set(have[i])
    if flag:
        break
    resources |= add_resource
    time += 1
    
print(len(visited))
print(*sorted(list(visited)))

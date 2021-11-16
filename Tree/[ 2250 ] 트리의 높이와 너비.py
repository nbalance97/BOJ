import sys
from collections import deque


input = lambda: sys.stdin.readline().rstrip()
N = int(input())
left_child = [-1] * (N+1)
right_child = [-1] * (N+1)
p = set([i for i in range(1, N+1)])

for i in range(N):
    a, b, c = map(int, input().split())
    left_child[a] = b
    right_child[a] = c
    if b in p:
        p.remove(b)
    if c in p:
        p.remove(c)

root_node = list(p)[0]
child_count = [-1] * (N+1)
pos = [0] * (N+1)

def get_chk_child(p):
    count = 0
    if left_child[p] != -1:
        count += get_chk_child(left_child[p])
    if right_child[p] != -1:
        count += get_chk_child(right_child[p])
    child_count[p] = count + 1
    return count + 1

def allow_number(p, left, right):
    pos[p] = left

    if left == right:
        pos[p] = left
        return
    
    if left_child[p] != -1:
        pos[p] = left+child_count[left_child[p]]

    if left_child[p] != -1:
        allow_number(left_child[p], left, pos[p]-1)

    if right_child[p] != -1:
        allow_number(right_child[p], pos[p]+1, right)

get_chk_child(root_node)
allow_number(root_node, 1, N)
step = [[] for _ in range(10001)]
queue = deque([[root_node, 0]])
while queue:
    nx, s = queue.popleft()
    step[s].append(pos[nx])
    if left_child[nx] != -1:
        queue.append([left_child[nx], s+1])
    if right_child[nx] != -1:
        queue.append([right_child[nx], s+1])

level = 1
answer = 1
for i in range(10001):
    step[i].sort()
    if len(step[i]) > 1:
        if answer < step[i][-1] - step[i][0] + 1:
            answer = step[i][-1] - step[i][0] + 1
            level = i+1

print(level, answer)

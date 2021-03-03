import sys

n = int(sys.stdin.readline().rstrip())
tree = list(map(lambda x: int(x),sys.stdin.readline().rstrip().split()))
del_tree = int(sys.stdin.readline().rstrip())

DELETE = -5

def is_parent(node, check):
    idx = node
    while True:
        if tree[idx] == check:
            return True
        elif tree[idx] == -1:
            return False
        else:
            idx = tree[idx]

tree[del_tree] = DELETE
child = [0] * n
candidate = []

for i in range(n):
    if i == del_tree:
        continue
    if is_parent(i, del_tree): # 삭제된 노드의 자식 노드인 경우 모두 DELETE 처리
        candidate.append(i)

for i in candidate:
    tree[i] = DELETE

for i in range(n): # 자식 노드의 수 계산
    if tree[i] == -1: # 루트노드 제외
        continue
    
    if tree[i] == DELETE: # 제거노드와 구분
        child[i] = DELETE
    else:
        child[tree[i]] += 1 # 자식 노드의 수 증가

leef = 0
for i in range(n):
    if child[i] == 0:
        leef += 1
        
print(leef)

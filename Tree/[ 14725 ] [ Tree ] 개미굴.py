import sys

class node:
    def __init__(self, element):
        self.element = element
        self.child = dict()

input = lambda: sys.stdin.readline().rstrip()
N = int(input())
root = node(0)

for _ in range(N):
    sequence = input().split()[1:]

    temp = None

    if root.child.get(sequence[0]) == None:
        root.child[sequence[0]] = node(sequence[0])
    temp = root.child[sequence[0]]
    
    for i in range(1, len(sequence)):
        if temp.child.get(sequence[i]) == None:
            temp.child[sequence[i]] = node(sequence[i])
        temp = temp.child[sequence[i]]

def solve(node, level):
    child_list = sorted(node.child.keys())
    prefix = '--' * (level - 1)
    if level >= 1:
        print(prefix + node.element)
    for each_child in child_list:
        solve(node.child[each_child], level+1)

solve(root, 0)
    
    

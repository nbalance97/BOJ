import sys

sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

class tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.element = 0

        
        
idx = 0
s = ''

def solve(po, io, left, right):
    global idx
    if left > right:
        return None
    temp = tree()
    temp.element = po[idx]
    pos = io.index(po[idx], left, right+1)
    idx += 1
    if left == right:
        return temp
    temp.left = solve(po, io, left, pos-1)
    temp.right = solve(po, io, pos+1, right)
    return temp

def postorder(root):
    global s
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    # 여기서 바로 출력 안해주고 join으로 했다가 문제생김ㅠㅠ 숫자가 2자리 이상일때 join은 안됨..
    print(root.element, end=" ")

for _ in range(T):
    n = int(input())
    s, idx = '', 0
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    root = solve(preorder, inorder, 0, n-1)
    postorder(root)
    print("")

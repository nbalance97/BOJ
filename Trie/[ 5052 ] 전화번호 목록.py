import sys

input = lambda: sys.stdin.readline().rstrip()

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.end = False


T = int(input())
for _ in range(T):
    N = int(input())
    callnumbers = [input() for _ in range(N)]
    callnumbers.sort(key = lambda x:len(x))
    root = TreeNode("r")
    flag = True
    for callnumber in callnumbers:
        temp = root
        for ch in callnumber:
            if temp.children.get(ch) == None:
                temp.children[ch] = TreeNode(ch)
                temp = temp.children[ch]
            else:
                temp = temp.children[ch]
                if temp.end:
                    flag = False
                    break
        temp.end = True
        if not flag:
            break
    if flag:
        print('YES')
    else:
        print('NO')
                    
    

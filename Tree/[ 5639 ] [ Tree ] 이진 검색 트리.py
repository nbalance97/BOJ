import sys

sys.setrecursionlimit(10**5)

class tree_node():
    def __init__(self, element):
        self.left = None
        self.right = None
        self.element = element


def push_tree(tree, element):
    if tree.element == None: # 맨 위 루트노드는 초깃값 None
        tree.element = element
    else:
        temp = tree_node(element)
        while True:
            # 현재 트리의 요소보다 입력값이 크면 오른쪽
            if tree.element < element:
                if tree.right == None:
                    tree.right = temp
                    break
                else:
                    tree = tree.right
            # 작으면 왼쪽
            else:
                if tree.left == None:
                    tree.left = temp
                    break
                else:
                    tree = tree.left

def post_order(tree):
    if tree == None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.element)
                
Tree = tree_node(None)
while True:
    try:
        p = int(input())
        push_tree(Tree, p)
    except:
        break

post_order(Tree)

        
    

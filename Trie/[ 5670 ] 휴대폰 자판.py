
from collections import deque

class Trie:
    def __init__(self, alpha):
        self.isword = False
        self.child = {}

def make_trie(root, word):
    temp = root
    for alpha in word:
        if temp.child.get(alpha) == None:
            temp.child[alpha] = Trie(alpha)
        temp = temp.child[alpha]
    temp.isword = True

def calc_word(root, word):
    temp = root
    movement = 0
    for i in range(len(word)):
        if i == 0:
            temp = temp.child[word[i]]
            movement += 1
            continue
        
        if len(temp.child) == 1:
            if temp.isword:
                temp = temp.child[word[i]]
                movement += 1
            else:
                temp = temp.child[word[i]]
        else:
            temp = temp.child[word[i]]
            movement += 1
            
    return movement
        

while True:
    try:
        N = int(input())
        words = [input() for _ in range(N)]
        root = Trie(0)
        for word in words:
            make_trie(root, word)

        total_movement = 0
        for word in words:
            total_movement += calc_word(root, word)
        print("%.2f"%(total_movement / len(words)))
    except:
        break

import sys
from itertools import combinations

input = sys.stdin.readline

while True:
    p = list(map(int, sys.stdin.readline().rstrip().split()))
    if p[0] == 0:
        break

    p = p[1:]
    # 후보에서 6개 뽑아서 조합(로또)
    temp = combinations(p, 6)
    for t in temp:
        print(*t) # *로 표시하면 (랑 ,는 빼서 출력됨
    print()
    
    

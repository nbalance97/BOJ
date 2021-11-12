'''
리스트를 정렬한 다음, 홀수번째 인덱스와 짝수번째 인덱스 따로 저장
짝수번째 인덱스는 그대로 추가, 홀수번째 인덱스는 뒤집어서 뒤에 추가하면 된다.
이후 최대 차이를 구한 다음 출력
'''

import sys

input = lambda: sys.stdin.readline().rstrip()
N = int(input())

for _ in range(N):
    C = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    left = trees[1::2]
    right = trees[0::2]
    make_tree = right + left[::-1]
    answer = 0
    for i in range(C):
        answer = max(answer,
                     abs(make_tree[i]-make_tree[(i-1)%C]),
                     abs(make_tree[(i+1)%C]-make_tree[i]))
    print(answer)

import sys

input = sys.stdin.readline

n = int(input().rstrip())

temp = [[' '] * (n*2+1) for _ in range(n+1)]


def draw(top, down, left, right):
    for i in range(left, right+1):
        temp[down][i] = '*';
    temp[down-1][left+1] = '*';
    temp[down-1][right-1] = '*';
    temp[down-2][left+2] = '*';

def recursion(top, down, left, right):
    if down-top == 2 and right-left == 4:
        draw(top, down, left, right)
        return

    height_mid = (top + down) // 2 # 가운데 위치
    width_mid = (left + right) // 2 # 가운데 너비
    add_b = (down-top) // 2 # 4등분 햇을때 위쪽 블럭

    recursion(top, height_mid, left+add_b+1, right-add_b-1)
    recursion(height_mid+1, down, left, width_mid-1)
    recursion(height_mid+1, down, width_mid+1, right)

recursion(1, n, 1, (n*2)-1) 

# 문제 되는 출력 부분
''' 
for i in range(1, len(temp)): 
    for j in range(1, len(temp[i])):
        print(temp[i][j], end="")
    print()
'''

# print문 최소화해야 시간초과 안걸림..
for i in range(1, len(temp)):
    print("".join(temp[i][1:]))

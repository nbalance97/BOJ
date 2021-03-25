import sys

input = sys.stdin.readline

N, r, c = map(int, input().rstrip().split())

count = 0
flag = False
def recursion(lr, rr, lc, rc):
    global count, r, c, flag
    if flag:
        return
    if lr == rr and lc == rc:
        if lr == r and lc == c:
            flag = True
        return

    
    mid_r = (lr + rr) // 2
    mid_c = (lc + rc) // 2

    block = ((rr-lr) // 2 + 1) ** 2

    if lr <= r and mid_r >= r and lc <= c and mid_c >= c:
        recursion(lr, mid_r, lc, mid_c)
    elif lr <= r and mid_r >= r and mid_c+1 <= c and rc >= c:
        count += block
        recursion(lr, mid_r, mid_c+1, rc)
    elif mid_r+1 <= r and rr >= r and lc <= c and mid_c >= c:
        count += block * 2
        recursion(mid_r+1, rr, lc, mid_c)
    elif mid_r+1 <= r and rr >= r and mid_c+1 <= c and rc >= c:
        count += block * 3
        recursion(mid_r+1, rr, mid_c+1, rc)

recursion(0, (2**N)-1, 0, (2**N)-1)
print(count)

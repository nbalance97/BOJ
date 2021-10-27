import sys

N = int(sys.stdin.readline().rstrip())
answer_list = []
def movement(n, src, dest, temp):
    if n <= 0:
        return

    movement(n-1, src, temp, dest)
    answer_list.append([src, dest])
    movement(n-1, temp, dest, src)


if N <= 20:
    print(2**N - 1)
    movement(N, 1, 3, 2)
    for a,b in answer_list:
        print(a, b)
else:
    print(2**N - 1)
    


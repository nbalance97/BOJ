import sys
from collections import defaultdict

input = lambda: sys.stdin.readline().rstrip()
n = int(input())
for i in range(n):
    M = input()
    counter = defaultdict(lambda: 0)

    check = True
    next_flg = False
    next_chr = ''
    for ch in M:
        if not check:
            break
        if next_flg:
            if ch != next_chr:
                check = False
            next_flg = False
            continue
        counter[ch] += 1
        if counter[ch] % 3 == 0:
            next_flg = True
            next_chr = ch
    # 다음에 문자가 하나 더 나와야 하는 경우
    if next_flg:
        check = False
    
    if check:
        print("OK")
    else:
        print("FAKE")

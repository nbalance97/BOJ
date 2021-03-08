import sys

input = sys.stdin.readline
L, C = map(int, input().rstrip().split())
sequence = list(map(str, input().rstrip().split()))
sequence.sort()

# recursion 돌면서 전체 탐색
def recursion(cur, seq, j=0, m=0):
    global L

    if len(cur) == L and j >= 2 and m >= 1:
        # 최소 자음 2자 이상 + 모음 1자 이상
        print(cur)
        return

    if len(seq) == 0: return

    if seq[0] in ["a", "e", "i", "o", "u"]:
        # 모음이라면 모음의 횟수를 m에 기록
        recursion(cur + seq[0], seq[1:], j, m + 1)
    else:
        # 자음이라면 자음의 횟수를 j에 기록
        recursion(cur + seq[0], seq[1:], j + 1, m)
    # 선택하지 않고 넘어감
    recursion(cur, seq[1:], j, m)

recursion("", sequence)
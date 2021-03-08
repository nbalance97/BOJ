import sys


# 실패 함수 구하는 함수( 실패 시 다음 인덱스 어디로 가야할지 표시 )
def createtable(pattern):
    table = [0] * len(pattern)
    p = 0
    for i in range(1, len(pattern)):
        while p > 0 and pattern[i] != pattern[p]:
            # 실패 함수 구할때도 KMP 알고리즘 활용하여서 계산
            p = table[p - 1]

        if pattern[i] == pattern[p]:
            p += 1
            table[i] = p

    return table


while True:
    pattern = sys.stdin.readline().rstrip()
    if pattern == ".":
        break

    Table = createtable(pattern)
    length = len(pattern)

    # 기본적으로 length // (length - Table[length-1])로 값 나옴
    # ex) ababab : 001234 이므로 0이 1로 바뀌는 순간부터 반복 시작임.

    # 1. Table[length-1] == 0인 경우 특정 패턴의 반복으로 만들지 못함
    # 2. length % (length - Table[length-1]) 이 나누어 떨어지지 않는다면 못만듬.
    if Table[length-1] == 0 or length % (length - Table[length-1]) != 0:
        print(1)
    else:
        print(length // (length - Table[length-1]))

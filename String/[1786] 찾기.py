import sys

# 공백이 있는 문자열 처리를 위해 rstrip 대신 replace 사용
T = sys.stdin.readline().replace("\n", "")
P = sys.stdin.readline().replace("\n", "")

def make_table(P):
    # 접미사와 접두사가 같은 경우의 최대 길이
    list = [0] * len(P)
    p = 0
    for i in range(1, len(P)):
        while p > 0 and P[p] != P[i]:
        # 접미사와 접두사가 다른 경우 나올때까지 접미사를 좌측으로 이동함.
        # 이부분을 그냥 p = p - 1 하면 틀림 나옴 ..
            p = list[p-1]

        # 접미사와 접두사가 같은 경우 접미사 부분을 오른쪽으로 한칸 이동
        if P[i] == P[p]:
            p = p + 1
            list[i] = p

    return list


table = make_table(P)
print(table)
j = 0
count = 0
answer = []

for i in range(len(T)):
    # 패턴과 문자열이 같지 않은 경우 비교를 시작해야 하는 곳으로 이동
    while j > 0 and P[j] != T[i]:
        j = table[j - 1]

    # 같은 경우 j 증가 및 문자 탐지에 성공했다면 다시 j 세팅
    if P[j] == T[i]:
        if j == len(P) - 1:
            answer.append(i - j + 1)
            j = table[j]
        else:
            j += 1


print(len(answer))
print(" ".join(list(map(str, answer))))

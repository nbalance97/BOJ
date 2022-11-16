import sys
import decimal

readline = sys.stdin.readline

n: int = int(readline())
buildings: list[int] = list(map(int, readline().split()))

answer = 0

for i in range(len(buildings)):
    count: int = 0
    for j in range(len(buildings)):
        if j == i:
            continue

        # i, j에 대응하는 직선의 방정식을 구해야 함
        startX: int = min(i, j)
        startY: int = max(i, j)

        a = (buildings[startX] - buildings[startY]) / (startX - startY)
        b = buildings[startY] - (a * startY)

        # i ~ j 사이에 존재하는 빌딩이 접하는지 체크해야 함
        for k in range(startX+1, startY):
            if k == i:
                continue

            #print(i, j, k, a * k + b, buildings[k])
            if a * k + b <= buildings[k]:
                break
        else:
            # print(i, j)
            count = count + 1

    # print(i, count)
    answer = max(answer, count)

print(answer)

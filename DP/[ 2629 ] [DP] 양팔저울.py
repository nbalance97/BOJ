import sys

input = sys.stdin.readline

weights_count = int(input().rstrip())
weights = list(map(int, input().rstrip().split()))

marbles_count = int(input().rstrip())
marbles = list(map(int, input().rstrip().split()))

dp = [False] * 40001
dp[0] = True

weights.reverse() # 역순으로 전환

for weight in weights:
    canmake = set()
    for i in range(40001):
        if dp[i] == True:
            if i + weight <= 40001:
                canmake.add(i+weight) # 오른쪽에 놓았을때,
            if i - weight >= 0:
                canmake.add(i-weight) # 왼쪽에 놓았을 때
            if weight - i >= 0:
                canmake.add(weight-i) # 현재 물체만 오른쪽에 두고 나머지는 왼쪽에 두었을 때
    for c in canmake:
        dp[c] = True

for marble in marbles:
    if dp[marble] == True:
        print('Y', end=" ")
    else:
        print('N', end=" ")

import sys

input = sys.stdin.readline
n = int(input().rstrip())

color = [[0, 0, 0]]
INT_MAX = sys.maxsize

for _ in range(n):
    color.append(list(map(int, input().rstrip().split())))

cost = INT_MAX
for init_color in range(3): # 1번 집 색상을 빨강, 파랑, 초록 각각 해봄.
    dp = [[INT_MAX] * 3 for _ in range(n+1)]
    dp[1][init_color] = color[1][init_color] # 초기 색상에 대해서만 수정. 나머지는 INT_MAX

    for t in range(2, n+1): # dp 테이블 채움. INT_MAX 처리 된 것들은 알아서 처리될듯.
        dp[t][0] = min(dp[t-1][1], dp[t-1][2]) + color[t][0]
        dp[t][1] = min(dp[t-1][0], dp[t-1][2]) + color[t][1]
        dp[t][2] = min(dp[t-1][0], dp[t-1][1]) + color[t][2]
        # 마지막 n번째 집은 n-1과 1번 집과 비교해야 하므로 따로 진행
        if t == n:
            dp[t][init_color] = INT_MAX

    c = min(dp[n])
    cost = min(c, cost)

print(cost)

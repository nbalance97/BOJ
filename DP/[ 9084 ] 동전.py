import sys

input = lambda : sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    coin_count = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [1] + [0] * M
    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i-coin]
        
    print(dp[M])
                


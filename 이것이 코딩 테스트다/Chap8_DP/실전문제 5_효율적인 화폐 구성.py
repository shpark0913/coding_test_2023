N, M = map(int, input().split())

coins = [int(input()) for _ in range(N)]

dp = [10001] * (M + 1)
dp[0] = 0

for i in range(N):
    for j in range(coins[i], M + 1):
        if dp[j - coins[i]] != 10001:
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

print(-1) if dp[M] == 10001 else print(dp[M])
N = int(input())

storage = list(map(int, input().split()))

dp = [0] * (N + 1)

dp[1], dp[2] = storage[0], max(storage[0], storage[1])

for i in range(3, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + storage[i - 1])

print(dp[N])
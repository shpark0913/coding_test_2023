N, M, K = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

cnt = 0
ans = 0
for _ in range(M):
    if cnt == K:
        cnt = 0
        ans += numbers[-2]
    else:
        cnt += 1
        ans += numbers[-1]

print(ans)

# 5 8 3
# 2 4 5 4 6
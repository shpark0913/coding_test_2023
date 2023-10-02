N, M = map(int, input().split())

cards = [list(map(int, input().split())) for _ in range(N)]

minmax = 0
for i in range(len(cards)):
    if min(cards[i]) > minmax:
        minmax = min(cards[i])

print(minmax)

# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4
from itertools import combinations

# 0 : 빈칸 / 1 : 집 / 2 : 치킨집

# N by N / 최대 M개의 치킨집
N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

homes = []
chickens = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            homes.append((i, j))
        if maps[i][j] == 2:
            chickens.append((i, j))

def get_chicken_distance():
    chickens_combs = list(combinations(chickens, M))
    answers = []
    for chicken_comb in chickens_combs:
        all_dist = 0
        for home in homes:
            dist = int(1e9)
            for comb in chicken_comb:
                temp = abs(comb[0] - home[0]) + abs(comb[1] - home[1])
                if temp < dist:
                    dist = temp
            all_dist += dist
        answers.append(all_dist)
    return answers

answers = get_chicken_distance()
print(min(answers))



# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2


# 5 2
# 0 2 0 1 0
# 1 0 1 0 0
# 0 0 0 0 0
# 2 0 0 1 1
# 2 2 0 1 2


# 5 1
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
# 1 2 0 0 0
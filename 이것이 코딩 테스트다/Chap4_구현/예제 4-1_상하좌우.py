# N = int(input())

# plans = input().split()

# i, j = 1, 1

# for plan in plans:
#     if plan == "L" and 1 < j:
#         j -= 1
#     elif plan == "R" and j < N:
#         j += 1
#     elif plan == "U" and 1 < i:
#         i -= 1
#     elif plan == "D" and i < N:
#         i += 1

# print(i, j)

########################################

n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny

print(x, y)
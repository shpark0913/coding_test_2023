N = int(input())

x, y = 0, 0

# 상 하 좌 우
move_types = ["U", "D", "L", "R"]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

plans = list(input().split())

for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            nx, ny = x + dx[i], y + dy[i]
    if 0 <= nx < N and 0 <= ny < N:
        x, y = nx, ny

print(x + 1, y + 1)



# 5
# R R R U D D
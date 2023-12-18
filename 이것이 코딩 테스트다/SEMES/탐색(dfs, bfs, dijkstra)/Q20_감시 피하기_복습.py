N = int(input())

maps = [list(input().split()) for _ in range(N)]

teachers_location = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == "T":
            teachers_location.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_student(x, y):
    for i in range(4):
        for j in range(1, N + 1):
            nx, ny = x + j * dx[i], y + j * dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if maps[nx][ny] == "S":
                    return True
                if maps[nx][ny] == "W":
                    break
            else:
                break
    return False

ans = "NO"

def dfs(count):
    global ans
    if count == 3:
        temp = set()
        for x, y in teachers_location:
            temp.add(find_student(x, y))
            if temp == {False}:
                ans = "YES"
        return
    for i in range(N):
        for j in range(N):
            if maps[i][j] == "X":
                maps[i][j] = "W"
                count += 1
                dfs(count)
                maps[i][j] = "X"
                count -= 1

dfs(0)

print(ans)

# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X
# YES

# 4
# S S S T
# X X X X
# X X X X
# T T T X
# NO  
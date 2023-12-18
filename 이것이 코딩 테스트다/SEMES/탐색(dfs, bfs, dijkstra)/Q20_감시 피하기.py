from itertools import combinations

n = int(input())
board = []      # 복도 정보
teachers = []   # 선생님 위치 정보
spaces = []     # 빈 공간 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == "T":
            teachers.append((i, j))
        if board[i][j] == "X":
            spaces.append((i, j))

# 좌 우 상 하 순서 
def watch(x, y, direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "W":
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "W":
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if board[x][y] == "S":
                return True
            if board[x][y] == "W":
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == "S":
                return True
            if board[x][y] == "W":
                return False
            x += 1
    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False

for data in combinations(spaces, 3):
    # 장애물 설치하기
    for x, y in data:
        board[x][y] = "W"

    if process() == False:
        find = True
        break

    # 장애물 삭제
    for x, y in data:
        board[x][y] = "X"

if find:
    print("YES")
else:
    print("NO")


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
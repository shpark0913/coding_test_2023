import copy

N, K = map(int, input().split())    # N by N / 1 ~ K 바이러스

maps = [list(map(int, input().split())) for _ in range(N)]
temp = [[0] * N for _ in range(N)]

S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def infection():
    global maps, temp
    for k in range(1, K + 1):
        for i in range(N):
            for j in range(N):
                if maps[i][j] == k:
                    temp[i][j] = k
                    for l in range(4):
                        nx, ny = i + dx[l], j + dy[l]
                        if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 0 and temp[nx][ny] == 0:
                            temp[nx][ny] = k
    maps = temp

for _ in range(S):
    infection()

print(maps[X - 1][Y - 1])

# 1. temp를 maps 정보에 따라 감염
# 2. maps를 temp로 대체
# 3. s번 반복

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

# 3


# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2

# 0
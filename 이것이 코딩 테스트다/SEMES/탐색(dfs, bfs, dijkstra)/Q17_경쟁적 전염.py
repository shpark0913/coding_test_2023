import copy

# 인덱스가 아님! 왼쪽 맨 위는 (0, 0)이 아니라 (1, 1)

# N X N 행렬, K : 1 ~ K 번 바이러스
N, K = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

# S초 후 (X, Y)에 존재하는 바이러스 종류는?
S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# target(바이러스의 종류), graph, 좌표 입력하면 상하좌우 감염
def virus(target, graph, x, y):
    graph[x][y] = target
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
            graph[nx][ny] = target

def infection():
    global maps
    temp = copy.deepcopy(maps)
    s = 0
    while 1:
        for k in range(1, K + 1):
            for i in range(N):
                for j in range(N):
                    if maps[i][j] == k:
                        virus(k, temp, i, j)
        s += 1
        maps = temp
        if s == S:
            return
infection()
print(maps[X - 1][Y - 1])

# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2
#
# 3
#
# ==========
#
# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 1 2 2
#
# 0
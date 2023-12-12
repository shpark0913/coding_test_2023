from collections import deque

# N X N 행렬, K : 1 ~ K 번 바이러스
N, K = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]

# S초 후 (X, Y)에 존재하는 바이러스 종류는?
S, X, Y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph):
    q = deque([])
    for k in range(1, K + 1):
        for i in range(N):
            for j in range(N):
                if graph[i][j] == k:
                    q.append((i, j, 1))
    while q:
        a, b, t = q.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if t > S: continue
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
                graph[nx][ny] = graph[a][b]
                q.append((nx, ny, t + 1))

bfs(maps)

print(maps)
print(maps[X-1][Y-1])
            


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
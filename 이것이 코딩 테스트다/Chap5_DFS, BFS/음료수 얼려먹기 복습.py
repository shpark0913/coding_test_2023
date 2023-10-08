from collections import deque

N, M = map(int, input().split())

ice = []

for _ in range(N):
    i = list(map(int, input()))
    ice.append(i)

num = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y):
    global num
    num += 1
    graph[x][y] = 1
    queue = deque([[x, y]])
    while queue:
        q = queue.popleft()
        for i in range(4):
            nx, ny = q[0] + dx[i], q[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                queue.append([nx, ny])
                graph[nx][ny] = 1

for n in range(N):
    for m in range(M):
        if ice[n][m] == 0:
            bfs(ice, n, m)

print(num)

# 4 5
# 00110
# 00011
# 11111
# 00000

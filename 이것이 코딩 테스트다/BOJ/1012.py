from collections import deque

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, x, y, N, M):
    global cnt
    cnt += 1
    graph[x][y] = 2
    queue = deque()
    queue.append([x, y])
    while queue:
        q = queue.popleft()
        for i in range(4):
            nx, ny = q[0] + dx[i], q[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 2
                queue.append([nx, ny])

for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                bfs(graph, i, j, N, M)

    print(cnt)
    
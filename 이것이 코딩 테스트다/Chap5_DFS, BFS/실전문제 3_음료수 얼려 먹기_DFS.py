N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0

def DFS(graph, visited, i, j):
    visited[i][j] = True
    graph[i][j] = 1
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and visited[nx][ny] == False:
            DFS(graph, visited, nx, ny)

for i in range(N):
    for j in range(M):
        if not graph[i][j]:
            count += 1
            DFS(graph, visited, i, j)

print(count)

# 4 5
# 00110
# 00011
# 11111
# 00000

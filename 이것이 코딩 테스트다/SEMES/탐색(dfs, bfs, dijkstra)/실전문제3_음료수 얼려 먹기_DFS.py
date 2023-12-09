N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, visited, a, b):
    visited[a][b] = True
    for i in range(4):
        nx, ny = a + dx[i], b + dy[i]
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 0:
            visited[nx][ny] = True
            dfs(graph, visited, nx, ny)

answer = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == 0:
            dfs(graph, visited, i, j)
            answer += 1

print(answer)

# 4 5
# 00110
# 00011
# 11111
# 00000
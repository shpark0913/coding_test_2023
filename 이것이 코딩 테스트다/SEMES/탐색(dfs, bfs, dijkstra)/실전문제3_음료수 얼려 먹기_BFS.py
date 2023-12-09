from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, visited, a, b):
    visited[a][b] = True
    queue = deque([(a, b)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == "0":
                visited[nx][ny] = True
                queue.append((nx, ny))

N, M = map(int, input().split())

graph = [list(input()) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

answer = 0

for i in range(N):
    for j in range(M):
        if not visited[i][j] and graph[i][j] == "0":
            bfs(graph, visited, i, j)
            answer += 1

print(answer)

# 4 5
# 00110
# 00011
# 11111
# 00000
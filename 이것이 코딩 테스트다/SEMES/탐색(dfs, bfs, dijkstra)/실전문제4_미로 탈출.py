from collections import deque

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, visited, x, y):
    visited[x][y] = 1
    queue = deque([(x, y)])
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx, ny = a + dx[i], b + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and graph[nx][ny] == 1:
                visited[nx][ny] = visited[a][b] + 1
                queue.append((nx, ny))

bfs(graph, visited, 0, 0)

print(visited[-1][-1])

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
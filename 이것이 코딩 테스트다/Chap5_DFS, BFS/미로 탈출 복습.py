from collections import deque
N, M = map(int, input().split())

maze = []

for _ in range(N):
    m = list(map(int, input()))
    maze.append(m)

visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, visited, x, y):
    queue = deque([[x, y]])
    visited[x][y] = 1
    while queue:
        q = queue.popleft()
        for i in range(4):
            nx = q[0] + dx[i]
            ny = q[1] + dy[i]
            if 0 <= nx < N and  0 <= ny < M and not visited[nx][ny] and graph[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = visited[q[0]][q[1]] + 1

bfs(maze, visited, 0, 0)

# print(visited)
print(visited[N - 1][M - 1])


# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
from collections import deque

N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]

visited = [[False] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(maze, visited, i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    while queue:
        q = queue.popleft()
        a, b = q[0], q[1]
        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = visited[a][b] + 1

BFS(maze, visited, 0, 0)
print(visited[N - 1][M - 1])


# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
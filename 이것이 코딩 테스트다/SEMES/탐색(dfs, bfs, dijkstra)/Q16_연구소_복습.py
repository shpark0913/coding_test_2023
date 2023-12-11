from collections import deque

N, M = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]
temp = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs_virus(graph, visited, a, b):
    visited[a][b] = True
    queue = deque([(a, b)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0 and not visited[nx][ny]:
                graph[nx][ny] = 2
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_safe(graph):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                cnt += 1
    return cnt

answer = set()

def dfs(count):
    if count == 3:
        visited = [[False] * M for _ in range(N)]
        for i in range(N):
            for j in range(M):
                temp[i][j] = maps[i][j]

        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    bfs_virus(temp, visited, i, j)
        safe_zone = count_safe(temp)
        answer.add(safe_zone)
        return
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                count += 1
                dfs(count)
                maps[i][j] = 0
                count -= 1

dfs(0)

print(max(answer))

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0 

# 27

# 4 6
# 0 0 0 0 0 0
# 1 0 0 0 0 2
# 1 1 1 0 0 2
# 0 0 0 0 0 2

# 9

# 8 8
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 2 0 0 0 0 0 0 2
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0

# 3

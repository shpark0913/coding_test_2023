from collections import deque

# N by N / L 이상 R 이하 => 국경 개방
N, L, R = map(int, input().split())

maps = [list(map(int, input().split())) for _ in range(N)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, visited, a, b):
    spots = [(a, b)]
    people_num = graph[a][b]
    union_num = 1
    visited[a][b] = True
    queue = deque([(a, b)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    people_num += graph[nx][ny]
                    union_num += 1
                    spots.append((nx, ny))
    for spot in spots:
        graph[spot[0]][spot[1]] = int(people_num / union_num)

cnt = 0
while 1:
    bfs_num = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs_num += 1
                bfs(maps, visited, i, j)
    if bfs_num == N ** 2:
        print(cnt)
        break
    cnt += 1

    

# 2 20 50
# 50 30
# 20 40
#1

# 2 40 50
# 50 30
# 20 40
#0

# 2 20 50
# 50 30
# 30 40
#1

# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10
#2

# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10
#3
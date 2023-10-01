N, M = map(int, input().split())

A, B, d = map(int, input().split())

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maps = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

count = 1

while 1:
    # 현재 위치 방문 처리
    visited[A][B] = 1
    cnt = 0
    for _ in range(4):
        cnt += 1
        d -= 1
        if d < 0: d = 3
        nx = A + dx[d]
        ny = B + dy[d]
        if visited[nx][ny] == 0 and maps[nx][ny] == 0:
            A, B = nx, ny
            count += 1
            break
    if cnt == 4:
        nx = A - dx[d]
        ny = B - dx[d]
        if visited[nx][ny] == 1:
            break
        else:
            A, B = nx, ny

print(count)

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
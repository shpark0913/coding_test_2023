from collections import deque

N, M = map(int, input().split())

areas = [list(map(int, input())) for _ in range(N)]

cnt = 0
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if not areas[i][j]:
            areas[i][j] = 1
            cnt += 1
            queue.append([i, j])
            while queue:
                q = queue.popleft()
                for k in range(4):
                    nx = q[0] + dx[k]
                    ny = q[1] + dy[k]
                    if nx >= 0 and nx < N and ny >= 0 and ny < M and not areas[nx][ny]:
                        queue.append([nx, ny])
                        areas[nx][ny] = 1

print(cnt)

# 4 5
# 00110
# 00011
# 11111
# 00000

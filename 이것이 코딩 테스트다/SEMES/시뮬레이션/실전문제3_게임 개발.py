N, M = map(int, input().split())

A, B, d = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maps = [list(map(int, input().split())) for _ in range(N)]
maps[A][B] = 2

def move(d):
    global A, B
    # 4방향 회전
    for _ in range(4):
        d -= 1
        if d < 0: d = 3
        nx, ny = A + dx[d], B + dy[d]
        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
            maps[nx][ny] = 2
            A, B = nx, ny
            return "NEXT"
    # 4방향 회전 실패 => 뒤로 가기
    nx, ny = A - dx[d], B - dy[d]
    if 0 <= nx < N and 0 <= ny < M:
        if maps[nx][ny] == 0:
            maps[nx][ny] = 2
            A, B = nx, ny
        else:
            return "FINISH"
    else:
        return "FINISH"

while 1:
    ans = move(d)
    if ans == "FINISH":
        answer = 0
        for i in range(N):
            for j in range(M):
                if maps[i][j] == 2:
                    answer += 1
        print(answer)
        break

# 1. 반시계 방향 회전 후 직진 가능한지 탐색
# 2. 1을 4번했을 때  실패하면 뒤로 가는 로직 추가
# 3. 2가 실패하면 리턴

# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1
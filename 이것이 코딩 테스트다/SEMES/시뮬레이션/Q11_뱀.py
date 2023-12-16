from collections import deque

# 상(0) 우(1) 하(2) 좌(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())

# 0 : 빈 칸 / 1 : 사과
graph = [[0] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
direction = 1
snake = deque([(0, 0)])

##################################################

K = int(input())    # 사과의 개수

for _ in range(K):
    a, b = map(int, input().split())
    graph[a - 1][b - 1] = 1

##################################################

L = int(input())    # 뱀의 방향 변환 횟수
moves = {}

# C의 의미 => D : 오른쪽 회전, L : 왼쪽 회전
for _ in range(L):
    X, C = input().split()
    moves[int(X)] = C

def snake_move(time, x, y):
    global direction
    nx, ny = x + dx[direction], y + dy[direction]
    # 벽에 꽈당
    if not (0 <= nx < N and 0 <= ny < N):
        print(time)
        return
    # 자신 몸에 꽈당
    if visited[nx][ny] == True:
        print(time)
        return
    
    # 사과 있다
    if graph[nx][ny] == 1:
        visited[nx][ny] = True
        snake.append((nx, ny))
    
    else:
        visited[nx][ny] = True
        snake.append((nx, ny))
        a, b = snake.popleft()
        visited[a][b] = False

    # 방향 설정
    if time in moves.keys():
        if moves[time] == "D":
            direction += 1
            if direction > 3:
                direction = 0
        else:
            direction -= 1
            if direction < 0:
                direction = 3
    
    snake_move(time + 1, nx, ny)

snake_move(1, 0, 0)


# 1. 앞으로 나간다.
# 1-1. 사과가 있다 => 길이가 길어진다
# 1-2. 사과가 없다 => 길이가 유지된다
# 2. moves에 방향 전환 => 방향 바꾼다

# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

# 10
# 4
# 1 2
# 1 3
# 1 4
# 1 5
# 4
# 8 D
# 10 D
# 11 D
# 13 L

# 10
# 5
# 1 5
# 1 3
# 1 2
# 1 6
# 1 7
# 4
# 8 D
# 10 D
# 11 D
# 13 L
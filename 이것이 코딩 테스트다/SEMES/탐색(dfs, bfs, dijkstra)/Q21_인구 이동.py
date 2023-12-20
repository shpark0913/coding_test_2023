from collections import deque

# N by N / 인구 차이 L 이상 R 이하 => 국경선 개방
N, L, R = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(graph, visited, a, b):
    all_countries = [(a, b)]
    people_num = graph[a][b]
    country_num = 1
    queue = deque([(a, b)])
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                visited[nx][ny] = True
                all_countries.append((nx, ny))
                people_num += graph[nx][ny]
                country_num += 1
                queue.append((nx, ny))
    return [all_countries, people_num, country_num]

move_times = 0

while 1:
    answers = []
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                answers.append(bfs(graph, visited, i, j))
    if len(answers) == N ** 2:
        break
    move_times += 1
    for answer in answers:
        all_countries, people_num, country_num = answer
        new_people_num = int(people_num / country_num)
        for country in all_countries:
            graph[country[0]][country[1]] = new_people_num

print(move_times)

# 2 20 50
# 50 30
# 20 40

# 1

# 2 40 50
# 50 30
# 20 40

# 0

# 2 20 50
# 50 30
# 30 40

# 1

# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10

# 2

# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10

# 3
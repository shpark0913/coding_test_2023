# 회사의 개수, 경로의 개수
N, M = map(int, input().split())

INF = int(1e9)

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B], graph[B][A] = 1, 1

# 1번 회사 -> K번 회사 소개팅 -> X 회사 방문
X, K = map(int, input().split())

for i in range(1, N + 1):
    graph[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # if graph[i][j] > graph[i][k] + graph[k][j]:
            #     graph[i][j] = graph[i][k] + graph[k][j]
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

print(graph[1][K] + graph[K][X]) if graph[1][K] + graph[K][X] < INF else print(-1)

# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5

# 4 2
# 1 3
# 2 4
# 3 4

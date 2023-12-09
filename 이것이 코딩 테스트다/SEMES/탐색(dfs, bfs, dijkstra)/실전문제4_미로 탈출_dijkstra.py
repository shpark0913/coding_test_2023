import heapq

N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

distance = [[int(1e9)] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(graph, a, b):
    distance[a][b] = 1
    q = []
    heapq.heappush(q, (1, (a, b)))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        dist, now = heapq.heappop(q)
        if distance[now[0]][now[1]] < dist: continue
        for i in range(4):
            nx, ny = now[0] + dx[i], now[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                cost = dist + 1
                if distance[nx][ny] > cost:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, (nx, ny)))

dijkstra(graph, 0, 0)

print(distance[-1][-1])

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111
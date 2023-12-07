import heapq

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
N, M, K, X = map(int, input().split())

INF = int(1e9)

graph = [[] for _ in range(N + 1)]

distance = [INF] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(X)

answer = []

for i in range(1, N + 1):
    if distance[i] == K:
        answer.append(i)

if len(answer):
    for a in answer:
        print(a)
else: print(-1)
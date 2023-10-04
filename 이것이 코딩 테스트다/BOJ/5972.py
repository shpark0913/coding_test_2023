import heapq

N, M = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for j in graph[now]:
            if distance[j[0]] > distance[now] + j[1]:
                distance[j[0]] = distance[now] + j[1]
                heapq.heappush(q, (distance[j[0]], j[0]))

dijkstra(1)

print(distance[N])
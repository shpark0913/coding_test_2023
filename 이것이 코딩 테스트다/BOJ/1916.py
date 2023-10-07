import heapq

N = int(input())
M = int(input())

INF = int(1e9)

distance = [INF] * (N + 1)

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, arrive = map(int, input().split())

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for j in graph[now]:
            if distance[j[0]] > distance[now] + j[1]:
                distance[j[0]] = distance[now] + j[1]
                heapq.heappush(q, (distance[j[0]], j[0]))

dijkstra(start)

print(distance[arrive])
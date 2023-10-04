import heapq

# 지름길의 수, 고속도로의 길이
N, D = map(int, input().split())

INF = int(1e9)

distance = [INF] * (10001)

graph = [[] for _ in range(10001)]

for i in range(D):
    graph[i].append((i + 1, 1))

for i in range(N):
    a, b, c = map(int, input().split())
    if a > D or b > D: continue
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for i in graph[now]:
            if distance[i[0]] > distance[now] + i[1]:
                distance[i[0]] = distance[now] + i[1]
                heapq.heappush(q, (distance[i[0]], i[0]))

dijkstra(0)

min_value = INF
for i in range(1, D + 1):
    if distance[i] != INF:
        if min_value > distance[i] + (D - i):
            min_value = distance[i] + D - i

print(min_value)
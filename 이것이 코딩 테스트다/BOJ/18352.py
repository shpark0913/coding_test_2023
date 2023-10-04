import heapq

INF = int(1e9)

# 노드의 개수, 간선의 개수, 거리 정보, 시작 도시
N, M, K, X = map(int, input().split())

distance = [INF] * (N + 1)

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in graph[now]:
            if distance[i[0]] > distance[now] + i[1]:
                distance[i[0]] = distance[now] + i[1]
                heapq.heappush(q, (distance[i[0]], i[0]))

dijkstra(X)

answer = []
for i in range(1, len(distance)):
    if distance[i] == K:
        answer.append(i)
answer.sort()

if answer:
    for a in answer:
        print(a)
else: print(-1)

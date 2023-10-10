import heapq

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

for _ in range(TC := int(input())):
    # 컴퓨터 개수, 의존성 개수, 첫 해킹 컴퓨터
    n, d, com = map(int, input().split())

    INF = int(1e9)

    graph = [[] for _ in range(n + 1)]

    distance = [INF] * (n + 1)
    for _ in range(d):
        a, b, c = map(int, input().split())
        graph[b].append((a, c))

    dijkstra(com)

    num = 0
    time = 0

    for d in distance:
        if d != INF:
            num += 1
            if d  > time:
                time = d

    print(num, time)


# 2
# 3 2 2
# 2 1 5
# 3 2 5
# 3 3 1
# 2 1 2
# 3 1 8
# 3 2 4
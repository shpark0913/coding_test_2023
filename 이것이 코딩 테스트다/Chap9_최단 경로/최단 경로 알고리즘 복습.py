# # 기본 다익스트라
# INF = int(1e9)

# N, M = map(int, input().split())

# start = int(input())

# graph = [[] for _ in range(N + 1)]

# visited = [False] * (N + 1)

# distance = [INF] * (N + 1)

# for _ in range(M):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# def get_smallest_node():
#     index = 0
#     min_value = INF
#     for i in range(1, N + 1):
#         if distance[i] < min_value and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     visited[start] = 0
#     distance[start] = 0
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for _ in range(N - 1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = graph[now] + j[1]
#             if distance[j[0]] > cost:
#                 distance[j[0]] = cost
            

#########################################################

# # heapq 사용 다익스트라

# import heapq

# INF = int(1e9)

# N, M = map(int, input().split())

# start = int(input())

# graph = [[] for _ in range(N + 1)]

# distance = [INF] * (N + 1)

# for _ in range(M):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# def dijkstra(start):
#     q = []
#     distance[start] = 0
#     heapq.heappush(q, (0, start))
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist: continue
#         for j in graph[now]:
#             cost = dist + j[1]
#             if distance[j[0]] > cost:
#                 distance[j[0]] = cost
#                 heapq.heappush(q, (cost, j[0]))


#########################################################


# 플로이드 워셜 알고리즘

INF = int(1e9)

N, M = map(int, input().split())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
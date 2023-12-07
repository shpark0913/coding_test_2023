# DFS
# def dfs(graph, visited, v):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             visited[i] = True
#             dfs(graph, visited, i)


####################################################


# BFS
# from collections import deque

# def bfs(graph, visited, v):
#     queue = deque([v])
#     visited[v] = True
#     while queue:
#         q = queue.popleft()
#         for i in graph[q]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)


####################################################


# Dijkstra
import heapq

INF = int(1e9)

N, M = map(int, input().split())

start = int(input())

graph = [[] for _ in range(N + 1)]

distance = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))  # a에서 b로 가는 비용 : c

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

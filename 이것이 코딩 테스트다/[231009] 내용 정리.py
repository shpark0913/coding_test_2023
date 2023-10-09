# # DFS 복습

# def dfs(graph, visited, v):
#     visited[v] = True
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, visited, i)


######################################################


# # BFS 복습
# from collections import deque

# def bfs(graph, visited, v):
#     visited[v] = True
#     queue = deque()
#     queue.append(v)
#     while queue:
#         q = queue.popleft()
#         for i in graph[q]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)


######################################################


# # 다익스트라 기본
# INF = int(1e9)
# N, M = map(int, input().split())
# start = int(input())
# visited= [False] * (N + 1)
# distance = [INF] * (N + 1)
# graph = [[] for _ in range(N + 1)]

# for _ in range(M):
#     a, b, c = map(int, input().split())
#     graph[a].append((b, c))

# def get_smallest_node():
#     index = 0
#     min_value = INF
#     for i in range(1, N + 1):
#         if min_value > distance[i] and not visited[i]:
#             min_value = distance[i]
#             index = i
#     return index

# def dijkstra(start):
#     visited[start] = True
#     distance[start] = 0
#     # 처음에만 해당 과정 추가하는 것 기억
#     for j in graph[start]:
#         distance[j[0]] = j[1]
#     for _ in range(N - 1):
#         now = get_smallest_node()
#         visited[now] = True
#         for j in graph[now]:
#             cost = distance[now] + j[1]
#             if distance[j[0]] > cost:
#                 distance[j[0]] = cost


######################################################


# # heapq 이용한 다익스트라
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
#     distance[start] = 0
#     q = []
#     heapq.heappush(q, (0, start))
#     while q:
#         dist, now = heapq.heappop(q)
#         if distance[now] < dist: continue
#         for j in graph[now]:
#             cost = dist + j[1]
#             if distance[j[0]] > cost:
#                 distance[j[0]] = cost
#                 heapq.heappush(q, (cost, j[0]))


######################################################


# # 플로이드 워셜
# N, M = map(int, input().split())

# INF = int(1e9)

# graph = [[INF] * (N + 1) for _ in range(N + 1)]

# for i in range(1, N + 1):
#     graph[i][i] = 0

# for _ in range(M):
#     a, b, c = map(int, input().split())
#     graph[a][b] = c

# for k in range(1, N + 1):
#     for a in range(1, N + 1):
#         for b in range(1, N + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


from itertools import permutations, combinations, product, combinations_with_replacement

data = ["A", "B", "C"]

result_permutations = list(permutations(data, 3))

result_combinations = list(combinations(data, 3))

result_product = list(product(data, repeat=3))

result_combinations_with_replacement = list(combinations_with_replacement(data, 3))

print(result_permutations)
print(result_combinations)
print(result_product)
print(result_combinations_with_replacement)
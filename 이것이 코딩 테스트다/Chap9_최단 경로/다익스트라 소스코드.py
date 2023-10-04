INF = int(1e9)

# 노드, 간선의 개수
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

start = int(input())

visited = [False] * (n + 1)

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append(b, c)

def get_smallest_node():
    index = 0
    min_value = INF
    for i in range(1, n + 1):
        # not visited[i] 계속 까먹네. 주의하자
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    for i in graph[start]:
        distance[i[0]] = i[1]
    for i in range(n - 1):
        now = get_smallest_node()
        # visited[now] = True 잊지 말자.
        visited[now] = True
        for j in graph[now]:
            if distance[j[0]] > distance[now] + j[1]:
                distance[j[0]] = distance[now] + j[1]

dijkstra(start)



###############################################################################################

import heapq

INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

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

dijkstra(start)
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

graph = [[] for _ in range(n + 1)]

visited = [False] * (n + 1)

distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append(b, c)

def get_smallest_node():
    index = 0
    min_value = INF
    for i in range(1, n + 1):
        # visited[i] 처리 꼭 할 것!
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    visited[start] = True
    distance[start] = 0
    for j in graph[start]:
        distance[j[0]] = j[1]
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if distance[j[0]] > cost:
                distance[j[0]] = cost

dijkstra(start)

print(distance[1:])
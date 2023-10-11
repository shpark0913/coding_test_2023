from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

def bfs(graph, visited, v, c):
    visited[v] = c
    queue = deque()
    queue.append(v)
    while queue:
        q = queue.popleft()
        for j in graph[q]:
            if not visited[j]:
                queue.append(j)
                visited[j] = c

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0

for i in range(1, N + 1):
    if len(graph[i]):
        for j in graph[i]:
            if not visited[j]:
                cnt += 1
                bfs(graph, visited, j, cnt)

print(max(visited[1:]) + visited[1:].count(False))
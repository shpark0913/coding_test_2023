from collections import deque

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

def bfs(graph, visited, v):
    visited[v] = 0
    queue = deque([v])
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                visited[i] = visited[q] + 1
                queue.append(i)

bfs(graph, visited, X)

print(visited)

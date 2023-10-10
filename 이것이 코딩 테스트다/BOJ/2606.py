from collections import deque

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, visited, v):
    visited[v] = True
    queue = deque()
    queue.append(v)
    while queue:
        q = queue.popleft()
        for j in graph[q]:
            if not visited[j]:
                visited[j] = True
                queue.append(j)

bfs(graph, visited, 1)

print(visited.count(True) - 1)

from collections import deque

def dfs(graph, visited, v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)

def bfs(graph, visited, i):
    queue = deque([i])
    visited[i] = True
    while queue:
        q = queue.popleft()
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)


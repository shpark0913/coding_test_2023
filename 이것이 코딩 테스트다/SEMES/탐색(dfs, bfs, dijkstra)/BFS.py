from collections import deque

def bfs(graph, visited, v):
    queue = deque([v])
    visited[v] = True
    while queue:
        q = queue.popleft()
        print(q, end=' ')
        for i in graph[q]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

graph = [
    [],
    [2, 3, 8], 
    [1, 7],
    [1, 4, 5],
    [3, 5], 
    [3, 4], 
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, visited, 1)
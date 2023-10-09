N = int(input())

start, end = map(int, input().split())

M = int(input())

graph = [[] for _ in range(N + 1)]

visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(graph, visited, v):
    for j in graph[v]:
        if not visited[j]:
            visited[j] = visited[v] + 1
            dfs(graph, visited, j)

dfs(graph, visited, start)

print(visited[end]) if visited[end] else print(-1)

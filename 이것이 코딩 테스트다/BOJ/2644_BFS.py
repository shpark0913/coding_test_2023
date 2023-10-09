from collections import deque

N = int(input())

start, end = map(int, input().split())

M = int(input())

graph = [[] for _ in range(N + 1)]

visited = [False] * (N + 1)

def bfs(graph, visited, v):
    visited[v] = 1
    queue = deque()
    queue.append(v)
    while queue:
        q = queue.popleft()
        for j in graph[q]:
            if not visited[j]:
                queue.append(j)
                visited[j] = visited[q] + 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, visited, start)

print(visited[end] - 1) if visited[end] != False else print(-1)
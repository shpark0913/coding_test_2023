from collections import deque

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

def bfs(visited, graph, v):
    queue = deque([v])
    visited[v] = True
    while queue:
        q = queue.popleft()
        print(q, end = " ")
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(visited, graph, 1)


# def dfs(visited, graph, v):
#     # 현재 노드 방문
#     visited[v] = True
#     print(v, end=" ")
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(visited, graph, i)

# dfs(visited, graph, 1)

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
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

answer = []

for i in range(1, len(visited)):
    if visited[i] == K:
        answer.append(i)

if answer:
    for a in answer:
        print(a)
else:
    print(-1)

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

# 4 3 2 1
# 1 2 
# 1 3
# 1 4

# 4 4 1 1
# 1 2
# 1 3
# 2 3
# 2 4
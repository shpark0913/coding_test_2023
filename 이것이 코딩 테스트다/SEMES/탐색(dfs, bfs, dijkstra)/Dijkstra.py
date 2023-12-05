import heapq

INF = int(1e9)

# 노드, 간선의 개수
n, m = map(int, input().split())

# 시작 노드 번호
start = int(input())

# 노드 간의 관계
graph = [[] for _ in range(n + 1)]

distance = [[INF] * (n + 1)]

# 간선 정보
for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하며, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # 가장 최단 거리가 짧은 노드에 대해 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적 있는 노드라면 무시
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

import heapq
import sys

start = 1
n, m = map(int, input().split())  # n : 정점 / m: 간선

graph = [[] for _ in range(n + 1)]
graph_v = []

for _ in range(m):
    a, b, c = map(int, input().split())
    # 방향성 없는 그래프는 양방향 모두 추가
    graph[a].append((b, c))
    graph[b].append([a, c])

v1, v2 = list(map(int, input().split()))

INF = sys.maxsize


def dijkstra(start):
    distance = [INF] * (n + 1)

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dest, now = heapq.heappop(q)

        for i, j in graph[now]:
            if distance[i] < j:
                continue

            cost = dest + j
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    return distance


total_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = total_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = total_distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)
print(result if result < INF else -1)

if __name__ == "__main__":
    pass

# 4 6
# 1 2 3
# 2 3 3
# 3 4 1
# 1 3 5
# 2 4 5
# 1 4 4
# 2 3

import heapq
import sys


def soulution():
    n, m = map(int, input().split())  # n : 정점의 개수 / m : 간선의 개수
    start = int(input())
    INF = sys.maxsize
    distance = [INF] * (n + 1)

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dest, now = heapq.heappop(q)

        if distance[now] < dest:
            continue

        for x, y in graph[now]:
            if dest + y < distance[x]:
                distance[x] = dest + y
                heapq.heappush(q, (dest + y, x))

    for i in range(1, n + 1):
        print('INF' if distance[i] == INF else distance[i])


if __name__ == "__main__":
    soulution()

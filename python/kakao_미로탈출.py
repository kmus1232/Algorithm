from heapq import *

INF = 1e10


def dijkstra(n, start, end, graph, traps):
    pq = []
    heappush(pq, (0, start, 0))  # (cost, src, status)
    visited = [[False] * (1 << len(traps)) for _ in range(n + 1)]

    while pq:
        cost, now, status = heappop(pq)
        if now == end:
            return cost

        if now in traps:
            status ^= 1 << traps.index(now)
        if visited[now][status]:
            continue
        visited[now][status] = True

        for i in range(1, n + 1):
            if i == now:
                continue
            if (now in traps and (status & 1 << traps.index(now) != 0)) \
                    ^ (i in traps and (status & 1 << traps.index(i) != 0)):
                if graph[i][now] < INF:
                    heappush(pq, (cost + graph[i][now], i, status))
            else:
                if graph[now][i] < INF:
                    heappush(pq, (cost + graph[now][i], i, status))


def solution(n, start, end, roads, traps):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0
    for road in roads:
        src, dst, cost = road
        if cost < graph[src][dst]:
            graph[src][dst] = cost

    return dijkstra(n, start, end, graph, traps)


print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
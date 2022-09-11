import sys
import heapq

input = sys.stdin.readline


def dijkstra(graph, start):
    distance = [1e10] * len(graph)
    q = []
    heapq.heappush(q, (0, start))
    while q:
        cost, now = heapq.heappop(q)
        if cost < distance[now]:
            distance[now] = cost
            for nxt, nxt_cost in graph[now]:
                if distance[nxt] > cost + nxt_cost:
                    heapq.heappush(q, (cost + nxt_cost, nxt))

    return distance


n, m, party = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    src, dst, dist = map(int, input().split())
    graph[src].append((dst, dist))

shortest_to_party = [0] * (n + 1)
for i in range(1, n + 1):
    if i == party:
        continue
    shortest_to_party[i] = dijkstra(graph, i)[party]

shortest_from_party = dijkstra(graph, party)
longest_path = 0
for i in range(1, n + 1):
    longest_path = max(longest_path, shortest_to_party[i] + shortest_from_party[i])

print(longest_path)
import heapq


def solution(n, paths, gates, summits):
    gates, summits = set(gates), set(summits)
    graph = [[] for _ in range(n + 1)]
    for a, b, cost in paths:
        if a in gates or b in summits:
            graph[a].append((b, cost))
        elif a in summits or b in gates:
            graph[b].append((a, cost))
        else:
            graph[a].append((b, cost))
            graph[b].append((a, cost))

    intensities = [float("inf")] * (n + 1)
    q = []
    for gate in gates:
        intensities[gate] = 0
        q.append((0, gate))

    while q:
        cur_inten, cur = heapq.heappop(q)
        if cur_inten > intensities[cur]:
            continue

        for nxt, nxt_inten in graph[cur]:
            nxt_inten = max(nxt_inten, cur_inten)
            if nxt_inten < intensities[nxt]:
                intensities[nxt] = nxt_inten
                heapq.heappush(q, (nxt_inten, nxt))

    ans_sum, ans_inten = None, float("inf")
    for i, inten in enumerate(intensities):
        if i in summits and inten < ans_inten:
            ans_sum = i
            ans_inten = inten

    return ans_sum, ans_inten

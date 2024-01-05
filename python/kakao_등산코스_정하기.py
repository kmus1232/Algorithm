from collections import deque


def bfs(cut, G, ss, bgn, ext):
    vst = [0] * 50001
    q = deque(ss)

    last = float("inf")

    while q:
        now = q.popleft()
        for cost, nxt in G[now]:
            if cost > cut or vst[nxt] or bgn[nxt]:
                continue
            vst[nxt] = 1
            if ext[nxt]:
                last = min(last, nxt)
                continue
            q.append(nxt)

    if last != float("inf"):
        return last, True
    return None, False


def solution(n, paths, gates, summits):
    G = [[] for _ in range(50001)]

    for p in paths:
        G[p[0]].append((p[2], p[1]))
        G[p[1]].append((p[2], p[0]))

    ss = gates
    bgn = [0] * 50001
    ext = [0] * 50001

    for s in gates:
        bgn[s] = 1
    for e in summits:
        ext[e] = 1

    l, r = 1, 10000000
    top = None

    while l <= r:
        m = (l + r) // 2
        result, found = bfs(m, G, ss, bgn, ext)
        if found:
            top = result
            r = m - 1
        else:
            l = m + 1

    return [top, l]

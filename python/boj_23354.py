from typing import List
from collections import defaultdict
import heapq

N = int(input())
board = []
edges = defaultdict(list) # (r, c) -> [((nr, nc), cost), ((nr2, nc2), cost2), ...]
targets = [] # [(r1, c1), (r2, c2), ...]
home = None # (r, c)

# 보드를 채우면서, 탈영병과 부대의 위치를 저장한다 + 부대의 값을 0으로 바꾼다
for r in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for c in range(N):
        if row[c] == 0:
            targets.append((r, c))
        if row[c] == -1:
            home = (r, c)
            row[c] = 0

# 각 노드들을 연결하는 간선을 저장한다
for r in range(N):
    for c in range(N):
        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N): continue
            edges[(r, c)].append(((nr, nc), board[nr][nc])) # (연결된 노드, 비용) 을 저장


def dijkstra(r, c) -> List[List]:
    # 시작 위치를 받아서, 다른 모든 노드들에 대한 최단 경로를 담은 2차원 배열을 반환한다
    sp = [[float('inf')] * N for _ in range(N)]
    sp[r][c] = 0
    q = [(0, (r, c))]
    while q:
        dist, (cr, cc) = heapq.heappop(q)
        if dist > sp[cr][cc]: continue
        for (nr, nc), cost in edges[(cr, cc)]:
            if dist + cost < sp[nr][nc]:
                sp[nr][nc] = dist + cost
                heapq.heappush(q, (dist + cost, (nr, nc)))
    return sp


# 탈영병과 부대를 시작점으로 하는 2차원 최단거리 배열을 빌드한다
def build_sp(targets, home):
    sp_dict = dict()
    sp_dict[home] = dijkstra(*home)
    for target in targets:
        sp_dict[target] = dijkstra(*target)
    return sp_dict


# 부대에서 시작해 탈영병을 모두 잡고 부대로 돌아오는 가능한 모든 경로를 만든다.
def make_routes(targets, home):
    routes = []
    def f(route, targets, home):
        if not route:
            route.append(home)
            f(route, targets, home)
        elif not targets:
            routes.append(route + [home])
        else:
            for i in range(len(targets)):
                f(route + [targets[i]], targets[:i] + targets[i+1:], home)

    f([], targets, home)
    return routes


# 가능한 모든 경로들을 비교해 그중 최단 경로의 비용을 반환한다
def find_shortest_route(sp, routes):
    ans = float('inf')
    for route in routes:
        cost = 0
        for i in range(len(route) - 1):
            src, dst = route[i], route[i + 1]
            cost += sp[src][dst[0]][dst[1]]
        ans = min(ans, cost)

    return ans


sp = build_sp(targets, home)
routes = make_routes(targets, home)
ans = find_shortest_route(sp, routes)
print(ans)

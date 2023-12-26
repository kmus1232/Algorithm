from collections import defaultdict, deque
import sys

sys.setrecursionlimit(5000)

n = int(input())
graph = defaultdict(list)
for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cycle = set()
visit = set()
def find_cycle(prev, now, stack):
    if cycle: # 이미 사이클을 찾았다면 모든 탐색을 종료한다.
        return
    if now in visit:
        cycle.add(now)
        while stack and stack[-1] != now:
            cycle.add(stack.pop())
        return

    visit.add(now)
    for nxt in graph[now]:
        if nxt == prev:
            continue
        find_cycle(now, nxt, stack + [now])


find_cycle(None, 1, [])

def find_path_to_cycle(i):
    visit = set([i])
    q = deque([(i, 0)])
    while q:
        now, cost = q.popleft()
        for nxt in graph[now]:
            if nxt in cycle:
                return cost + 1
            if nxt in visit:
                continue
            visit.add(nxt)
            q.append((nxt, cost + 1))


ans = []
for i in range(1, n + 1):
    if i in cycle:
        ans.append(0)
    else:
        ans.append(find_path_to_cycle(i))

print(*ans)

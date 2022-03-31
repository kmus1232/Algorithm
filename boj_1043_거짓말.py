from collections import deque
from itertools import combinations

n, m = map(int, input().split())
people_who_know = set(list(map(int, input().split()))[1:])

parties = []
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    party = list(map(int, input().split()))[1:]
    parties.append(party)
    for a, b in combinations(party, 2):
        graph[a][b] = 1
        graph[b][a] = 1

visited = [False] * (n + 1)
for p in people_who_know:
    visited[p] = True
q = deque(people_who_know)
while q:
    now = q.popleft()
    for nxt in range(1, n + 1):
        connected = graph[now][nxt]
        if connected and not visited[nxt]:
            visited[nxt] = True
            q.append(nxt)

people_who_know.update([i for i in range(1, n + 1) if visited[i]])

ans = 0
for party in parties:
    is_able_to_lie = True
    for p in party:
        if p in people_who_know:
            is_able_to_lie = False
            break
    if is_able_to_lie:
        ans += 1

print(ans)

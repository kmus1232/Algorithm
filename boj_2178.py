from collections import deque

n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

diff = [(-1, 0), (1, 0), (0, -1), (0, 1)]

q = deque()
q.append((0, 0))
while q:
    x, y = q.popleft()
    if x == n - 1 and y == m - 1:
        print(graph[x][y])
        break

    for dx, dy in diff:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

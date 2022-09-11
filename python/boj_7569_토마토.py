import sys
from collections import deque

m, n, h = map(int, input().split())
box = []
not_rotten = 0
q = deque()
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
day_count = 0

for z in range(h):
    board = []
    for y in range(n):
        data = list(map(int, sys.stdin.readline().strip().split()))
        for x, t in enumerate(data):
            if t == 0:
                not_rotten += 1
            elif t == 1:
                q.append((z, y, x, 0))
        board.append(data)
    box.append(board)

while q:
    z, y, x, day = q.popleft()
    if day_count < day:
        day_count = day
    for i in range(6):
        nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
        if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
            if box[nz][ny][nx] == 0:
                not_rotten -= 1
                box[nz][ny][nx] = 1
                q.append((nz, ny, nx, day + 1))

if not_rotten > 0:
    print(-1)
else:
    print(day_count)

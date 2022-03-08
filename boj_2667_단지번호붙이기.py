from collections import deque, defaultdict


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input())))

cnt = 0
groups = defaultdict(int)
diff = [(0,1), (0,-1), (1,0), (-1,0)]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            cnt += 1
            groups[cnt] += 1
            board[i][j] = 0
            q = deque()
            q.append((i, j))
            while q:
                x, y = q.popleft()
                for dx, dy in diff:
                    nx = x + dx
                    ny = y + dy
                    if (0 <= nx < n) and (0 <= ny < n) and board[nx][ny] == 1:
                        board[nx][ny] = 0
                        groups[cnt] += 1
                        q.append((nx, ny))
print(cnt)
for v in sorted(groups.values()):
    print(v)
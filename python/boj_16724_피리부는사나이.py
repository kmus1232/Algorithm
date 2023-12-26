n, m = map(int, input().split())

dirs = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
board = [[None] * m for _ in range(n)]

for r in range(n):
    for c, d in enumerate(input()):
        dr, dc = dirs[d]
        nr, nc = r + dr, c + dc
        board[r][c] = (nr, nc)

visit = [[-1] * m for _ in range(n)]
count = 0

def dfs(r, c, i):
    if visit[r][c] == i:
        global count
        count += 1
        return
    elif visit[r][c] != -1:
        return

    visit[r][c] = i
    nr, nc = board[r][c]
    dfs(nr, nc, i)

i = 0
for r in range(n):
    for c in range(m):
        if visit[r][c] != -1:
            continue
        dfs(r, c, i)
        i += 1

print(count)

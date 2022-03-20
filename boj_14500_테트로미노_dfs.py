import sys

input = sys.stdin.readline


def dfs(r, c, idx, total):
    global ans
    if ans >= total + (3 - idx) * max_val:
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if idx == 1:
                    visited[nr][nc] = True
                    dfs(r, c, idx + 1, total + board[nr][nc])
                    visited[nr][nc] = False
                visited[nr][nc] = True
                dfs(nr, nc, idx + 1, total + board[nr][nc])
                visited[nr][nc] = False


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
ans = 0
max_val = max(map(max, board))

for r in range(N):
    for c in range(M):
        visited[r][c] = True
        dfs(r, c, 0, board[r][c])
        visited[r][c] = False

print(ans)

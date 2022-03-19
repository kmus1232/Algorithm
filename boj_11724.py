from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0] * N for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    board[u-1][v-1] = 1
    board[v-1][u-1] = 1

visited = [False] * N
ans = 0
for i in range(N):
    if visited[i]:
        continue

    ans += 1
    visited[i] = True
    stack = [i]
    while stack:
        now = stack.pop()
        for nxt in range(N):
            if board[now][nxt] == 1 and not visited[nxt]:
                visited[nxt] = True
                stack.append(nxt)

print(ans)
from collections import deque

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
shark = (0, 0)
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark = (i, j)
time_cnt = 0
eaten_fish_cnt = 0
shark_size = 2
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]


def find_fish(shark_location):
    visited = [[False] * N for _ in range(N)]
    r, c = shark_location
    visited[r][c] = True
    q = deque()
    q.append((r, c, 0))
    candidate = []
    min_cost = 0
    while q:
        r, c, cost = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                fish_size = board[nr][nc]
                if fish_size == 0 or fish_size == shark_size:
                    visited[nr][nc] = True
                    q.append((nr, nc, cost + 1))
                elif fish_size < shark_size:
                    if min_cost == 0:
                        min_cost = cost + 1
                        candidate.append((nr, nc))
                    elif cost + 1 == min_cost:
                        candidate.append((nr, nc))
    if not candidate:
        return (-1, -1), -1
    else:
        return min(sorted(candidate)), min_cost


while True:
    next_fish, cost = find_fish(shark)
    if next_fish == (-1, -1):
        print(time_cnt)
        break
    else:
        board[shark[0]][shark[1]] = 0
        board[next_fish[0]][next_fish[1]] = 9
        shark = next_fish

        time_cnt += cost
        eaten_fish_cnt += 1
        if eaten_fish_cnt == shark_size:
            shark_size += 1
            eaten_fish_cnt = 0

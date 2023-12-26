board = []
for _ in range(19):
    board.append(list(map(int, input().split())))

def check(r, c, dr, dc):
    if board[r][c] == 0:
        return False
    for i in range(1, 5):
        if board[r][c] != board[r + dr * i][c + dc * i]:
            return False
    nr, nc = r + dr * 5, c + dc * 5
    if 0 <= nr < 19 and 0 <= nc < 19 and board[r][c] == board[nr][nc]:
        # 6번째 원소가 같다면 승리 X
        return False
    nr, nc = r - dr, c - dc
    if 0 <= nr < 19 and 0 <= nc < 19 and board[r][c] == board[nr][nc]:
        # -1번째 원소가 같다면 승리 X
        return False
    return True

is_done = False
ans_val = ans_r = ans_c = 0

# 가로로 탐색, dr = 0, dc = 1
for r in range(19):
    for c in range(15):
        if board[r][c] != 0 and check(r, c, 0, 1):
            ans_val, ans_r, ans_c = board[r][c], r, c
            is_done = True
            break
    if is_done:
        break

if not is_done:
    # 세로로 탐색, dr = 1, dc = 0
    for r in range(15):
        for c in range(19):
            if check(r, c, 1, 0):
                ans_val, ans_r, ans_c = board[r][c], r, c
                is_done = True
                break
        if is_done:
            break

if not is_done:
    # 오른쪽 아래 대각으로 탐색, dr = 1, dc = 1
    for r in range(15):
        for c in range(15):
            if check(r, c, 1, 1):
                ans_val, ans_r, ans_c = board[r][c], r, c
                is_done = True
                break
        if is_done:
            break

if not is_done:
    # 오른쪽 위 대각으로 탐색, dr = -1, dc = 1
    for r in range(4, 19):
        for c in range(15):
            if check(r, c, -1, 1):
                ans_val, ans_r, ans_c = board[r][c], r, c
                is_done = True
                break
        if is_done:
            break

print(ans_val)
if ans_val != 0:
    print(ans_r + 1, ans_c + 1)

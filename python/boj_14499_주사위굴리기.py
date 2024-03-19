RIGHT, LEFT, UP, DOWN = 1, 2, 3, 4
drc = {RIGHT: (0, 1), LEFT: (0, -1), UP: (-1, 0), DOWN: (1, 0)}

ROW, COL, r, c, K = map(int, input().split())
board = []
for _ in range(ROW):
    board.append(list(map(int, input().split())))
commands = list(map(int, input().split()))


def check_bound(rbound, cbound, r, c):
    if 0 <= r < rbound and 0 <= c < cbound:
        return True
    return False


def roll_dice(cmd, row, col):
    drow, dcol = row[:], col[:]
    if cmd == RIGHT:
        col = [drow[3]] + drow[:3]
        row = [dcol[1], dcol[0], dcol[3], dcol[2]]
    elif cmd == LEFT:
        col = [drow[1], drow[0], drow[3], drow[2]]
        row = dcol[1:] + [dcol[0]]
    elif cmd == UP:
        col = dcol[1:] + [dcol[0]]
        row = [dcol[2], drow[1], dcol[0], drow[3]]
    else:  # cmd == DOWN
        col = [dcol[3]] + dcol[:3]
        row = [dcol[0], drow[1], dcol[2], drow[3]]
    return row, col


row = [0, 0, 0, 0]
col = [0, 0, 0, 0]
result = []

for cmd in commands:
    dr, dc = drc[cmd]
    nr, nc = r + dr, c + dc
    if not check_bound(ROW, COL, nr, nc):
        continue
    r, c = nr, nc
    row, col = roll_dice(cmd, row, col)

    if board[r][c] == 0:
        board[r][c] = col[2]
    else:
        col[2] = board[r][c]
        board[r][c] = 0
    result.append(col[0])

for e in result:
    print(e)

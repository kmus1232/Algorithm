from typing import List
from copy import deepcopy

def rotate(sticker) -> List[List[int]]:
    """
    시계방향으로 90도 회전시킨 스티커를 반환한다.
    """
    row, col = len(sticker), len(sticker[0])
    rotated = [[0] * row for _ in range(col)]
    for r in range(row):
        for c in range(col):
            rotated[c][row - r - 1] = sticker[r][c]
    return rotated

def is_matchable(board, sticker) -> (int, int):
    """
    보드에 스티커를 붙일 수 있는지 판별하고, 붙일 가장 왼쪽 위의 좌표를 반환한다.
    붙일 수 없다면 (-1, -1)을 반환한다.
    """
    brow, bcol = len(board), len(board[0])
    srow, scol = len(sticker), len(sticker[0])
    for br in range(brow):
        for bc in range(bcol):
            if br + srow > brow or bc + scol > bcol: # 해당 br, bc에서 시작하는 스티커가 보드 범위를 넘어가면 continue
                continue

            matchable = True
            for sr in range(srow):
                for sc in range(scol):
                    if board[br + sr][bc + sc] + sticker[sr][sc] >= 2:
                        matchable = False
                        break
                if not matchable:
                    break
            if matchable:
                return (br, bc)

    return (-1, -1)

def attach_sticker(board, sticker, brow, bcol) -> None:
    srow, scol = len(sticker), len(sticker[0])
    for sr in range(srow):
        for sc in range(scol):
            board[brow + sr][bcol + sc] += sticker[sr][sc]


board_row, board_col, k = map(int, input().split())
board = [[0] * board_col for _ in range(board_row)]

stickers = []
for _ in range(k):
    r, c = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(sticker)

for sticker in stickers:
    s = deepcopy(sticker)
    for _ in range(4):
        br, bc = is_matchable(board, s)
        if br != -1:
            attach_sticker(board, s, br, bc)
            break
        s = rotate(s)

ans = 0
for r in range(board_row):
    for c in range(board_col):
        if board[r][c] == 1:
            ans += 1

print(ans)

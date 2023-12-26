from typing import List
import sys
sys.setrecursionlimit(10000)

LOSE = False
WIN = True
dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def solution(board, aloc, bloc):
    return play(board, 'A', *aloc, *bloc, 0)[1]


def is_inbound(board, r, c):
    return True if 0 <= r < len(board) and 0 <= c < len(board[0]) else False


def judge(board, r, c) -> (bool, List):
    # 현재 위치한 칸의 값이 0이거나, 다음에 이동할 칸이 없다면 패배
    next_movable = []
    for dr, dc in dir:
        nr, nc = r + dr, c + dc
        if is_inbound(board, nr, nc) and board[nr][nc] == 1:
            next_movable.append((nr, nc))

    if board[r][c] == 0 or not next_movable:
        return (LOSE, [])
    else:
        return (WIN, next_movable)


def play(board, player, ar, ac, br, bc, cnt):
    if player == 'A':
        outcome, next_movable = judge(board, ar, ac)
        if outcome == LOSE:
            return (LOSE, cnt)

        board[ar][ac] = 0
        a_wins = []
        a_loses = []
        for nr, nc in next_movable:
            b_outcome, b_cnt = play(board, 'B', nr, nc, br, bc, cnt + 1)
            if b_outcome == WIN:
                a_loses.append(b_cnt)
            else:
                a_wins.append(b_cnt)
        board[ar][ac] = 1

        if not a_wins:
            return (LOSE, max(a_loses))
        else:
            return (WIN, min(a_wins))

    else: # player == 'B'
        outcome, next_movable = judge(board, br, bc)
        if outcome == LOSE:
            return (LOSE, cnt)

        board[br][bc] = 0
        b_wins = []
        b_loses = []
        for nr, nc in next_movable:
            a_outcome, a_cnt = play(board, 'A', ar, ac, nr, nc, cnt + 1)
            if a_outcome == WIN:
                b_loses.append(a_cnt)
            else:
                b_wins.append(a_cnt)
        board[br][bc] = 1

        if not b_wins:
            return (LOSE, max(b_loses))
        else:
            return (WIN, min(b_wins))

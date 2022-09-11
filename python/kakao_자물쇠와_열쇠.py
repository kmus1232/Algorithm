def solution(key, lock):
    for _ in range(4):
        if try_unlocking(key, lock):
            return True
        else:
            lock = rotate_arr(lock)
    return False


def try_unlocking(key, lock):
    m, n = len(key), len(lock)
    board = [[0 for _ in range(n + 2 * m)] for _ in range(n + 2 * m)]
    for r in range(n):
        for c in range(n):
            board[m + r][m + c] = lock[r][c]

    for r in range(1, m + n):
        for c in range(1, m + n):
            add_key(key, board, r, c)
            if check_lock(board, m, n):
                return True
            delete_key(key, board, r, c)
    return False


def add_key(key, board, r, c):
    for row in range(len(key)):
        for col in range(len(key)):
            board[r + row][c + col] += key[row][col]


def delete_key(key, board, r, c):
    for row in range(len(key)):
        for col in range(len(key)):
            board[r + row][c + col] -= key[row][col]


def check_lock(board, m, n):
    for r in range(m, m + n):
        for c in range(m, m + n):
            if board[r][c] != 1:
                return False
    return True


def rotate_arr(arr):
    n = len(arr)
    tmp_arr = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            tmp_arr[c][n - 1 - r] = arr[r][c]
    return tmp_arr

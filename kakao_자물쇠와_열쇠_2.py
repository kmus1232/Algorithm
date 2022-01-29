from copy import deepcopy

def solution(key, lock):
    m = len(key)
    n = len(lock)
    for _ in range(4):
        for i in range(-m + 1, n):
            for j in range(-m + 1, n):
                if check(key, lock, i, j, m, n):
                    return True
        key = rotate(key)
    return False


def check(key, lock, i, j, m, n):
    dump = deepcopy(lock)
    for r in range(i, i + m):
        if 0 <= r < n:
            for c in range(j, j + m):
                if 0 <= c < n:
                    dump[r][c] += key[r - i][c - j]
    for i in range(n):
        for j in range(n):
            if dump[i][j] != 1:
                return False
    return True


def rotate(arr):
    l = len(arr)
    rst = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            rst[j][l-1-i] = arr[i][j]
    return rst

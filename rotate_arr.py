arr = [
    [10, 11, 12, 13, 14],
    [20, 21, 22, 23, 24],
    [30, 31, 32, 33, 34],
    [40, 41, 42, 43, 44],
    [50, 51, 52, 53, 54]
]

def rotate_arr(arr):
    n = len(arr)
    tmp_arr = [[0 for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            tmp_arr[c][n - 1 - r] = arr[r][c]
    return tmp_arr

def rotate_arr_without_tmp_arr(arr):
    n = len(arr)
    for r in range(n // 2):
        for c in range(r, n - 1 - r):
            tmp = arr[r][c]
            arr[r][c] = arr[n-1-c][r]
            arr[n-1-c][r] = arr[n-1-r][n-1-c]
            arr[n-1-r][n-1-c] = arr[c][n-1-r]
            arr[c][n-1-r] = tmp
    return


rotate_arr_without_tmp_arr(arr)
for r in arr:
    print(r)

print()
for r in rotate_arr(arr):
    print(r)

def combination(arr, n):
    if n == 0:
        return [[]]

    res = []
    for i in range(len(arr)):
        elem = arr[i]
        rest_arr = arr[i + 1:]
        for c in combination(rest_arr, n - 1):
            res.append([elem] + c)

    return res


for e in combination([1, 2, 3, 4, 5], 2):
    print(e)
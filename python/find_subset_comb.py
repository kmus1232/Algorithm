def combination(arr, n):
    if n == 0:
        return [[]]

    rst = []
    for i in range(len(arr)):
        e = arr[i]
        rest_arr = arr[i + 1:]
        for c in combination(rest_arr, n - 1):
            rst.append([e] + c)
    return rst


def find_subsets(arr):
    rst = []
    for l in range(len(arr) + 1):
        for e in combination(arr, l):
            rst.append(e)
    return rst


arr = [1, 2, 3, 4]

for e in find_subsets(arr):
    print(e)

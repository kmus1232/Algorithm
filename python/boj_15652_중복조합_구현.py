def combination_with_repetition(arr, n):
    if n == 0:
        return [[]]

    result = []
    for i, e in enumerate(arr):
        for tmp in combination_with_repetition(arr[i:], n - 1):
            result.append([e] + tmp)

    return result


N, M = map(int, input().split())
for e in combination_with_repetition([i for i in range(1, N + 1)], M):
    for n in e:
        print(n, end=' ')
    print()

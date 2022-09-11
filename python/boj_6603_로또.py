def select(data):
    result = []

    def dfs(start, cnt, arr):
        if cnt == 6:
            result.append(arr)
            return

        for i in range(start, len(data)):
            dfs(i + 1, cnt + 1, arr + [data[i]])

    dfs(0, 0, [])
    return result


while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break

    result = select(data[1:])
    for rst in result:
        for n in rst:
            print(n, end=' ')
        print()
    print()

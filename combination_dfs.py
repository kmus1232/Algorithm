n, m = map(int, input().split())


def dfs(last, cnt, arr):
    if cnt == m:
        for e in arr:
            print(e, end=' ')
        print()
        return

    for i in range(last, n + 1):
        arr.append(i)
        dfs(i + 1, cnt + 1, arr)
        arr.pop()


dfs(1, 0, [])
n, m = map(int, input().split())


def dfs(s, cnt, arr):
    if cnt == m:
        print(arr)
        return

    for i in range(s, n + 1):
        dfs(i + 1, cnt + 1, arr + [i])


dfs(1, 0, [])
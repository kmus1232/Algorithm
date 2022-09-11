l = ['a', 'b', 'c']
visited = [False for _ in range(len(l))]
answer = []

def dfs(cnt, lst):
    if cnt == len(l):
        answer.append(lst)
        return

    for i, val in enumerate(l):
        if visited[i]:
            continue

        visited[i] = True
        dfs(cnt + 1, lst + [val])
        visited[i] = False

dfs(0, [])
print(answer)

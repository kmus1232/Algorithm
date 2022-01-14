l = ['a', 'b', 'c', 'd', 'e']
n = len(l)
r = 2
ans = []

def dfs(idx, lst):
    if len(lst) == r:
        ans.append(lst)
        return

    for i in range(idx, n):
        dfs(i + 1, lst + [l[i]])

dfs(0, [])
for e in ans:
    print(e)

import sys

input = sys.stdin.readline


def dfs(tree, visited, node, dist):
    if visited[node]:
        return -1, -1
    if len(tree[node]) == 1 and visited[tree[node][0][0]]:
        visited[node] = True
        return node, dist

    visited[node] = True
    result = []
    for nxt, cost in tree[node]:
        result.append(dfs(tree, visited, nxt, dist + cost))
    return max(result, key=lambda x: x[1])


def solution():
    n = int(input())
    tree = dict()
    for _ in range(n):
        data = list(map(int, input().split()))
        node, edges = data[0], data[1:-1]
        i = 0
        tree[node] = list()
        while i < len(edges):
            tree[node].append((edges[i], edges[i + 1]))
            i += 2

    node, _ = dfs(tree, [False] * (n + 1), 1, 0)
    _, cost = dfs(tree, [False] * (n + 1), node, 0)
    return cost


print(solution())

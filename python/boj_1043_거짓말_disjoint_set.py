def find_parent(x, parent):
    if x == parent[x]:
        return x

    parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union_parent(a, b, parent):
    a = find_parent(a, parent)
    b = find_parent(b, parent)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def union_arr(arr, parent):
    if len(arr) < 2:
        return

    a = arr[0]
    for b in arr[1:]:
        union_parent(a, b, parent)


def solution():
    n, m = map(int, input().split())
    parent = [i for i in range(n + 1)]
    know = list(map(int, input().split()))[1:]
    if not know:
        print(m)
        return
    union_arr(know, parent)

    parties = []
    for _ in range(m):
        party = list(map(int, input().split()))[1:]
        parties.append(party)
        union_arr(party, parent)

    ans = 0
    root = find_parent(know[0], parent)
    for party in parties:
        flag = True
        for p in party:
            if find_parent(p, parent) == root:
                flag = False
                break
        if flag:
            ans += 1

    print(ans)


solution()
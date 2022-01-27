from bisect import bisect_left, insort

languages = ["cpp", "java", "python"]
jobs = ["backend", "frontend"]
career = ["junior", "senior"]
foods = ["chicken", "pizza"]

def solution(info, query):
    table = {}
    for l in languages:
        table[l] = {}
        for j in jobs:
            table[l][j] = {}
            for c in career:
                table[l][j][c] = {}
                for f in foods:
                    table[l][j][c][f] = []

    for data in info:
        l, j, c, f, s = data.split()
        insort(table[l][j][c][f], int(s))

    result = []
    for q in query:
        l, _, j, _, c, _, f, s = q.split()
        s = int(s)
        result.append(calc(table, l, j, c, f, s))

    return result


def calc(table, l, j, c, f, s) -> int:
    rst = 0
    if l == "-":
        for item in languages:
            rst += calc(table, item, j, c, f, s)
    elif j == "-":
        for item in jobs:
            rst += calc(table, l, item, c, f, s)
    elif c == "-":
        for item in career:
            rst += calc(table, l, j, item, f, s)
    elif f == "-":
        for item in foods:
            rst += calc(table, l, j, c, item, s)
    else:
        idx = bisect_left(table[l][j][c][f], s)
        rst += len(table[l][j][c][f]) - idx
    return rst

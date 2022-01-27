from itertools import combinations

def solution(orders, course):
    ans = []
    table = {}
    for i in course:
        table[i] = {}
        for s in orders:
            for comb in combinations(sorted(s), i):
                comb = ''.join(comb)
                if comb not in table[i]:
                    table[i][comb] = 1
                else:
                    table[i][comb] += 1
    for i in course:
        if len(table[i]) == 0:
            continue
        biggiest = max(table[i].values())
        if biggiest < 2:
            continue
        for k in table[i].keys():
            if table[i][k] == biggiest:
                ans.append(k)

    return sorted(ans)
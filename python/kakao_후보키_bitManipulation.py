from functools import cmp_to_key

def solution(relation):
    n_row = len(relation)
    n_col = len(relation[0])

    candidates = []
    for i in range(1, 1 << n_col):
        if check_uniqueness(relation, n_row, n_col, i):
            candidates.append(i)

    candidates.sort(key=cmp_to_key(compare))
    ans = 0
    while candidates:
        subset = candidates[0]
        ans += 1
        candidates = [e for e in candidates if e & subset != subset]

    return ans

def check_uniqueness(relation, n_row, n_col, subset):
    for r1 in range(n_row - 1):
        for r2 in range(r1 + 1, n_row):
            is_same = True
            for c in range(n_col):
                if subset & 1 << c:
                    if relation[r1][c] != relation[r2][c]:
                        is_same = False
            if is_same:
                return False
    return True

def compare(i, j):
    cnt_i = bin(i).count('1')
    cnt_j = bin(j).count('1')
    return cnt_i - cnt_j
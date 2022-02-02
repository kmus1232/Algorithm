from itertools import combinations

def solution(relation):
    len_cols = len(relation[0])
    keys = []
    for i in range(1, len_cols + 1):
        for cols in combinations(range(len_cols), i):
            if check_uniqueness(relation, cols):
                if check_minimality(keys, set(cols)):
                    keys.append(set(cols))
    return len(keys)

def check_uniqueness(relation, cols):
    n = len(relation)
    result = set()
    for data in relation:
        result.add(tuple([data[c] for c in cols]))
    return True if len(result) == n else False

def check_minimality(keys, cols):
    for key in keys:
        if key & cols == key:
            return False
    return True

print(solution(
    [
        ["100","ryan","music","2"],
        ["200","apeach","math","2"],
        ["300","tube","computer","3"],
        ["400","con","computer","4"],
        ["500","muzi","music","3"],
        ["600","apeach","music","2"]
    ]
))
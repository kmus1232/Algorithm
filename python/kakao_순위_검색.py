from collections import defaultdict
from bisect import bisect_left, insort

def solution(info, query):
    table = defaultdict(list)
    for data in info:
        lang, job, exp, food, score = data.split()
        for l in [lang, '-']:
            for j in [job, '-']:
                for e in [exp, '-']:
                    for f in [food, '-']:
                        key = ' and '.join([l, j, e, f])
                        insort(table[key], int(score))

    rst = []
    for q in query:
        q = q.split()
        key = ' '.join(q[:-1])
        score = int(q[-1])
        idx = bisect_left(table[key], score)
        rst.append(len(table[key]) - idx)

    return rst

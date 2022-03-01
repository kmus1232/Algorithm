from bisect import bisect, insort
from collections import defaultdict


def find_query(words, query):
    start = query.replace('?', 'a')
    end = query.replace('?', 'z')
    start_idx = bisect(words, start)
    end_idx = bisect(words, end)
    return end_idx - start_idx


def solution(words, queries):
    word_dict = defaultdict(list)
    reversed_word_dict = defaultdict(list)
    for word in words:
        insort(word_dict[len(word)], word)
        insort(reversed_word_dict[len(word)], word[::-1])

    result = []
    for q in queries:
        if q[0] == '?':
            result.append(find_query(reversed_word_dict[len(q)], q[::-1]))
        else:
            result.append(find_query(word_dict[len(q)], q))
    return result

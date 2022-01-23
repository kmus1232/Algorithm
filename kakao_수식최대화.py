from typing import List
from itertools import permutations

def calculate(word_arr: List[str], op: str) -> List[str]:
    result = []
    for word in word_arr:
        if word.isnumeric() or word[0] == "-":
            if len(result) == 0 or result[-1] != op:
                result.append(word)
            else:
                operator = result.pop()
                word2 = result.pop()
                result.append(str(eval(word2 + operator + word)))
        else:
            result.append(word)
    return result


def expression_parser(s: str) -> List[str]:
    result = []
    tmp = ''
    for c in s:
        if c.isnumeric():
            tmp += c
        else: # when c is operator
            result.append(tmp)
            tmp = ''
            result.append(c)
    result.append(tmp)
    return result


def solution(expression: str) -> int:
    exp = expression_parser(expression)
    op_set = set()
    for w in exp:
        if not w.isnumeric():
            op_set.add(w)

    max_value = 0
    for p in permutations(op_set):
        copy = exp[:]
        for op in p:
            copy = calculate(copy, op)
        max_value = max(abs(int(copy[0])), max_value)

    return max_value
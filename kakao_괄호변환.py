def is_proper(p):
    stack = []
    for e in p:
        if e == ')':
            if len(stack) == 0:
                return False
            else:
                stack.pop()
        else:
            stack.append(e)
    return True if len(stack) == 0 else False


def find_u_v(w):
    left_count = 0
    right_count = 0
    for i, e in enumerate(w):
        if e == '(':
            left_count += 1
        else:
            right_count += 1
        if left_count == right_count:
            return w[:i + 1], w[i + 1:]
    

def process(u):
    ret = ""
    for e in u[1:-1]:
        if e == '(':
            ret += ')'
        else:
            ret += '('
    return ret


def solution(w):
    if w == '':
        return w

    u, v = find_u_v(w)
    if is_proper(u):
        return u + solution(v)
    else:
        return f"({solution(v)}){process(u)}"

DUMMY = 0
NODE = 1


def make_binary_tree(n: int) -> str:  # ex) '0011010'
    bn = bin(n)[2:]
    for l in [1, 3, 7, 15, 31, 63]:
        if len(bn) <= l:
            bn = bn.zfill(l)
            return bn


def check(s: str, l, r, level) -> (bool, int):
    if l == r:
        return (True, DUMMY if s[l] == "0" else NODE)

    m = (l + r) // 2
    lcheck = check(s, l, m - 1, level + 1)
    rcheck = check(s, m + 1, r, level + 1)

    if not (lcheck[0] and rcheck[0]):
        return (False, -1)

    if s[m] == "0":
        if level == 0 or (lcheck[1] == NODE or rcheck[1] == NODE):
            # 더미 노드는 루트 노드가 될 수 없으며, 진짜 노드를 자식으로 가질 수 없다
            return (False, -1)
        else:
            return (True, DUMMY)
    else:
        return (True, NODE)


def solution(numbers):
    ans = []
    for n in numbers:
        bin_tree = make_binary_tree(n)
        check_result = check(bin_tree, 0, len(bin_tree) - 1, 0)[0]
        if check_result:
            ans.append(1)
        else:
            ans.append(0)
    return ans

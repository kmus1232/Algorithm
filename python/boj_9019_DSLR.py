from collections import deque


def D(s: str) -> str:
    n = int(s) * 2 % 10000
    return str(n).zfill(4)


def S(s: str) -> str:
    n = int(s) - 1
    if n == -1:
        n = 9999
    return str(n).zfill(4)


def L(s: str) -> str:
    return s[1:] + s[0]


def R(s: str) -> str:
    return s[-1] + s[:-1]


def find_path(src: str, dst: str) -> str:
    funcs = [D, S, L, R]
    rst_set = set()
    q = deque()
    q.append((src, ''))
    cnt = 0
    while q:
        cnt += 1
        print(cnt, len(q))

        s, cmd = q.popleft()
        for f in funcs:
            rst = f(s)
            next_cmd = cmd + f.__name__
            if rst == dst:
                return next_cmd
            if rst not in rst_set:
                rst_set.add(rst)
                q.append((rst, next_cmd))


n = int(input())
for _ in range(n):
    src, dst = input().split()
    print(find_path(src.zfill(4), dst.zfill(4)))

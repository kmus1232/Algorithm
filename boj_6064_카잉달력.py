from math import gcd

N = int(input())


def solution(m, n, x, y):
    while x <= (m * n) // gcd(m, n):
        if (x - y) % n == 0:
            return x
        x += m
    return -1


for _ in range(N):
    m, n, x, y = map(int, input().split())
    print(solution(m, n, x, y))

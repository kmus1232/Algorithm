def solution(a, b, c) -> int:
    if b == 1:
        return a % c
    rst = solution(a, b // 2, c)
    rst *= rst
    if b % 2 == 1:
        rst *= a
    return rst % c


a, b, c = map(int, input().split())
print(solution(a, b, c))

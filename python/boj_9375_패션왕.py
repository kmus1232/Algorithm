N = int(input())

for _ in range(N):
    n = int(input())
    d = dict()
    for _ in range(n):
        cloth, category = input().split()
        if category in d:
            d[category] += 1
        else:
            d[category] = 1
    rst = 1
    for v in d.values():
        rst *= (v + 1)
    print(rst - 1)
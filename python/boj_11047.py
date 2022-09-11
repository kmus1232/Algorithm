n, k = map(int, input().split())

arr_coin = []
for _ in range(n):
    arr_coin.append(int(input()))

cnt = 0
for coin in arr_coin[::-1]:
    cnt += (k // coin)
    k %= coin
    if k == 0:
        break

print(cnt)
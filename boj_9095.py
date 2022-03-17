arr = []
n = int(input())

for _ in range(n):
    arr.append(int(input()))

max_n = max(arr)
dp = [0 for _ in range(max_n + 1)]
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4, max_n + 1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for e in arr:
    print(dp[e])

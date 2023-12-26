target, n = map(int, input().split())
cost_map = dict()
for _ in range(n):
    c, p = map(int, input().split())
    if p not in cost_map:
        cost_map[p] = c
    else:
        cost_map[p] = min(cost_map[p], c)

# dp[p] = c, p = 홍보한 사람 수, c = p명 홍보하는데 사용한 비용
dp = [float('inf')] * 1200
dp[0] = 0

for i in range(target + 1):
    for p, c in cost_map.items():
        if dp[i] + c < dp[i + p]:
            dp[i + p] = dp[i] + c

print(min(dp[target:]))
